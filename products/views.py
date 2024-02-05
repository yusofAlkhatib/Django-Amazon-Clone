from django.shortcuts import render , redirect
from django.views.generic import ListView , DetailView 

from .models import Product , Brand , Review , ProductImages
from .forms import ReviewForm

# Create your views here.
def product_list(request):
    product = Product.objects.all()
    return render(request,'list.html',{'data':product})


class ProductList(ListView):
    model = Product



class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_images"] = ProductImages.objects.filter(product=self.get_object())
        context['product_reviews'] = Review.objects.filter(product=self.get_object())
        return context
    



class BrandList(ListView):
    model = Brand


class BrandDetail(ListView):
    model = Product
    template_name = 'products/brand_detail.html'
    
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        querySet = super().get_queryset()
        querySet = querySet.filter(brand = brand)
        return querySet 
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
    



def add_product_review(request,slug): 
    product = Product.objects.get(slug=slug)

    if request.method =='Post':
        form = ReviewForm(request.Post)
        
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.product = product
            myform.save()

            return redirect(f'/products/{slug}')
    
