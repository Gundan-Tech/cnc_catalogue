from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q

# Your existing list view
def product_list(request):
    products = Product.objects.all() 
    categories = Category.objects.all()

    # Search Logic
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(Q(name__icontains=search_query))

    # Category Logic
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)

    return render(request, 'catalogue/product_list.html', {
        'products': products, 
        'categories': categories
    })

# NEW: The detail view
def product_detail(request, pk):
    # This grabs the specific product using its ID (pk), or shows a 404 Error if it doesn't exist
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalogue/product_detail.html', {'product': product})