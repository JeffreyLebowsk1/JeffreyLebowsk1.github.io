---
layout: default
title: Gallery
---

# Gallery

{% for album in site.data.gallery %}
    ## {{ album.album_name }}
    <div class="album">
        {% for image in album.images %}
            ![{{ image }}](/assets/gallery/{{ album.album_path }}{{ image }})
        {% endfor %}
    </div>
{% endfor %}
