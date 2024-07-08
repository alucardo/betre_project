from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail

from contacts.models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']


        # Check if user has made inquiry alredy
        if request.user.is_authenticated:
            user_id = request.user.id
            has_connected = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_connected:
                messages.error(request, 'You have already made connected for this listing')
                return redirect('listing', listing_id=listing_id)

        contact = Contact(
            listing_id=listing_id,
            listing=listing,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
        )

        contact.save()

        # Send email after save
        should_send_email = False # Don't send for now
        if should_send_email:
            send_mail(
                'Property listing inquiry',
                'Property listing has been sent.',
                'btre@example.com',
                ['btre_bok@example.com', 'btre_sell@example.com'],
                fail_silently=False,
            )

        messages.success(request, 'Realtor will contact you soon!')
        return redirect('listing', listing_id=listing_id)


    return redirect('listings')
