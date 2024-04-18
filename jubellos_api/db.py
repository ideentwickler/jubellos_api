from datetime import datetime, timedelta

from jubellos_api.models import ScratchTicket, ScratchTicketState, ScratchTicketDetails, ScratchTicketPrize

details_gift = ScratchTicketDetails(
    image="https://example.com/gift_detail_graphic",
    title="iPhone 15 Max gewonnen!",
    text="Du hast ein iPhone 15 Max gewonnen! Wir melden uns bei dir.",
    disclaimer={"title": "Hinweis", "text": "Wir kontaktieren dich in Kürze über die angegebene E-Mail Adresse."}
)

details_loyalty = ScratchTicketDetails(
    image="https://example.com/loyalty_detail_graphic",
    title="200 Treuepunkte gewonnen!",
    text="Du hast 200 Treuepunkte gewonnen! Wir haben sie dir bereits gutgeschrieben.",
    disclaimer={"title": "Hinweis", "text": "Du kannst die Treuepunkte ab sofort in deinem Konto einsehen und einlösen."}
)

scratch_tickets = [
        ScratchTicket(
            id="1",
            imageUrl="https://example.com/1",
            title="Jubellos is active & loyalty",
            validFrom=datetime.now().replace(hour=20) - timedelta(days=1),
            validTo=datetime.now() + timedelta(days=7),
            state=ScratchTicketState.OPEN,
            prize=ScratchTicketPrize.LOYALTY_POINTS,
            details=details_loyalty
        ),
        ScratchTicket(
            id="2",
            imageUrl="https://example.com/1",
            title="Jubellos is active & gift",
            validFrom=datetime.now().replace(hour=20) - timedelta(days=1),
            validTo=datetime.now() + timedelta(days=7),
            state=ScratchTicketState.OPEN,
            prize=ScratchTicketPrize.GIFT,
            details=details_gift
        ),
        ScratchTicket(
            id="3",
            imageUrl="https://example.com/1",
            title="Jubellos is active, played & loyalty",
            validFrom=datetime.now().replace(hour=20) - timedelta(days=1),
            validTo=datetime.now() + timedelta(days=7),
            state=ScratchTicketState.PLAYED,
            prize=ScratchTicketPrize.LOYALTY_POINTS,
            details=details_loyalty
        ),
        ScratchTicket(
            id="4",
            imageUrl="https://example.com/2",
            title="Jubellos is on countdown",
            validFrom=datetime.now().replace(hour=20) + timedelta(days=7),
            validTo=datetime.now() + timedelta(days=14),
            state=ScratchTicketState.OPEN,
            prize=ScratchTicketPrize.LOYALTY_POINTS,
            details=details_loyalty
        ),
    ]
