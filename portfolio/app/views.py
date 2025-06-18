from django.shortcuts import redirect, render
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

# def contact_form(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', '').strip()
#         email = request.POST.get('email', '').strip()
#         message = request.POST.get('message', '').strip()

#         # Basic validation
#         if not name or not email or not message:
#             messages.error(request, "All fields are required.")
#             return redirect('contact_form')  # Replace with your URL name

#         print(f"New Contact Message:\nName: {name}\nEmail: {email}\nMessage: {message}")

#         messages.success(request, "Your message has been sent successfully!")
#         return redirect('contact_form')  # Replace with your URL name

#     return render(request, 'contact.html')