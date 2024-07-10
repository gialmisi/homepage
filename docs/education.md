---
hide:
 - navigation
 - toc
---
# Education
{% for edu in load_data('activities.yaml')['educations'] %}
## {{ edu.degree }}
*{{ edu.institution }} ({{ edu.year }})*
{% if edu.details %}<br>{{ edu.details }}{% endif %}
{% endfor %}