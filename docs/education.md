---
hide:
 - navigation
---
## Education
{% for edu in load_data('activities.yaml')['educations'] %}
### {{ edu.degree }}
*{{ edu.institution }} ({{ edu.year }})*<br>
{{ edu.details }}<br>
[Link to thesis]({{ edu.url }})
{% endfor %}

## Teaching