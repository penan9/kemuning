{% extends 'header.html' %}

{% block myContent %}
    <style>
        h1 { color: lightyellow; }
        div { color: brown; margin-bottom: 10px }
    </style>
    <h1>Products</h1>
    <div class="row" style="overflow-y: scroll; height: 400px">

        {% for product in products%}
            <div class="col" style="width: 20rem;">
                <div class="card" style="width: 16rem;">
                    <img class="card-img-top" src="{{product.image_url}}" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">Product: {{product.name}}</h5>
                        <p class="card-text" style="font-size: 14px;">Price: ${{product.price}}/${{product.price2}}</p>
                        <p class="card-text" style="font-size: 14px;">Qty: {{product.stock}}{{product.unit}}</p>
                        <a href="../articles/" class="btn btn-primary">Procedure</a>
                    </div>
                </div>
            </div>
        {%endfor%}
    </div>
{% endblock %}
