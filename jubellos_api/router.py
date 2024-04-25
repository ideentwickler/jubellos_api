from fastapi import APIRouter, Depends, HTTPException

from jubellos_api.deps import get_api_key, get_authorization_header
from jubellos_api.models import ScratchTicket, GetPlayScratchTicket, PostPlayScratchTicket, ScratchTicketState, ScratchTicketDetails
from jubellos_api.db import scratch_tickets


router = APIRouter(dependencies=[Depends(get_api_key)])


@router.get("/scratchTickets")
def read_scratch_tickets() -> list[ScratchTicket]:
    """
    Endpunkt um alle Scratch Tickets zu erhalten.
    Offene Frage:
    - Bei den Coupons spielen wir bei Nicht-Registrierten Usern keinen CouponCode aus
    - Wie ist das App-seitig für die ScratchTickets vorgesehen?
    """
    return scratch_tickets


@router.post("/scratchTickets/play", dependencies=[Depends(get_authorization_header)])
def play_scratch_ticket(scratchticket: PostPlayScratchTicket) -> GetPlayScratchTicket:
    """
    Endpunkt um ein Scratch Ticket zu spielen.
    Kann nur aufgerufen werden, wenn:
    - Erfolgreiche User-Authentifizierung anhand des Bearer Tokens (Nur regisrierte Loyalty-User)
    - Das Scratch Ticket im Status "open" ist
    """
    scratch_ticket = next(
        (scratch_ticket for scratch_ticket in scratch_tickets if scratch_ticket.state == "open" and scratchticket.id == scratch_ticket.id),
        None
    )

    if not scratch_ticket:
        raise HTTPException(status_code=404, detail="Scratch Ticket not found or already played.")

    scratch_ticket.state = ScratchTicketState.PLAYED

    return GetPlayScratchTicket(image="https://dummyimage.com/600x600/861a21/fff.jpg?text=Gewonnen", prize=scratch_ticket.prize) # noqa


@router.get("/scratchTickets/{id}", dependencies=[Depends(get_authorization_header)])
def read_scratch_ticket(id: str) -> ScratchTicketDetails:
    """
    Endpunkt um weitere Details zu einem Scratch Ticket zu erhalten.
    Kann nur aufgerufen werden, wenn:
    - Erfolgreiche User-Authentifizierung anhand des Bearer Tokens (Nur regisrierte Loyalty-User)
    - Das Scratch Ticket im Status "played" ist
    """
    scratch_ticket = next(
        (scratch_ticket for scratch_ticket in scratch_tickets if scratch_ticket.id == id and scratch_ticket.state == ScratchTicketState.PLAYED),
        None
    )

    if not scratch_ticket:
        raise HTTPException(status_code=404, detail="Scratch Ticket not found or not played.")

    # reset state to open for testing purposes
    scratch_ticket.state = ScratchTicketState.OPEN

    return scratch_ticket.details

