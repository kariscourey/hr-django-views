def render():
    pass  # built-in django


def login_required(login_url):
    pass  # built-in django; from django.contrib.auth.decorators import


class Product:
    pass


class ListView:
    pass  #  built-in django; from django.views.___


class LoginRequiredMixin:
    pass  #  built-in django;


class ProductForm:
    pass  #  built-in django; from django import forms (in forms.py)


class HttpResponseRedirect:
    pass  # from django.http import HttpResponseRedirect


def get_object_or_404(value, pk, seller):
    pass  # built-in django; from django.shortcuts import get_object_or_404


class Http404:
    pass  # from django.http import Http404


@login_required(login_url="/login")
# decorators are superpowers (just functions that are called before your function is called)
# function passed in as an argument
# wraps our function with another function
# python feature
# gives function to a function
# https://docs.python.org/3/glossary.html#term-decorator
def list_seller_products(request):
    # IF the user isn't logged in,
    #   REDIRECT the request to the login page

    # GET the user who made the request
    user = request.user

    # SET products as the result of getting all products with this user as the seller
    products = Product.objects.filter(seller=user)
    # seller is an attribute of the Product "model"'s instance
    # not currently a variable in context

    # CREATE a context with products to use in the template
    context = {
        "products": products,
    }

    # RENDER the page into a response using the request, template, and context
    response = render(request, "products/list.html", context)

    # RETURN the response
    return response


# In inheritence, the custom implementations are added ON TOP of the base class. However, when you apply a decorator to a class, your class’s custom code is BELOW the one provided by the decorator. Therefore, you don’t override the decorating code but rather “underride” it (i.e., give it something it can replace).


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "products/list.html"
    context_object_name = "products"

    def get_queryset(self):
        products = Product.objects.filter(seller=self.request.user)
        return products


pk = 1  # to make func work


def list_seller_products(request):
    # IF the user isn't logged in,
    #   REDIRECT the request to the login page
    user = request.user

    # GET the object by the PK and user
    # IF we don't find
    #   Throw 404
    product = get_object_or_404(Product, pk=pk, seller=user)

    # CREATE a ProductFOrm instance
    form = ProductForm(request.POST or None, instance=product)
    # request.POST = dict of all fields when form submitted

    # IF form is valid, we are saving
    if form.is_valid():
        #   SAVE form data
        form.save()
        #   Redirect to the detail page
        return HttpResponseRedirect("/products/" + str(pk))

    # CREATE a context with form to fill out
    context = {"form": form}  # so we have access to the form in our template

    # RENDER the page into a response using the request, template, and context
    return render(request, "products/update.html", context)


class ProductUpdateView(UpdateView):
    model = Product
    fields = [
        "name",
        "description",
        "quantity",
        "image",
        "backorder_date",
        "discount_percent",
        "category",
    ]
    template_name = "products/update.html"
    success_url = "/products/"
    login_url = "/login/"

    # get object goes and gets object in the class
    # fetches the one based on primary key
    # if wanted to fetch based on the seller, need to override this function
    # call super so it gets object as normal
    # adjust as needed to get seller-specific
    def get_object(self, *args, **kwargs):
        # get Product object (instance of Product class)
        object = super().get_object(*args, **kwargs)
        # check that object's seller is current user
        if object.seller != self.request.user:
            # if not, raise error
            raise Http404
        # else, return object for use in view
        return object
