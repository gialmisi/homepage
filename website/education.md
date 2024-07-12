---
hide:
 - navigation
---
## Education
{% for edu in load_data('education.yaml')['educations'] %}
### {{ edu.degree }}
*{{ edu.institution }} ({{ edu.year }})*<br>
[Link to thesis]({{ edu.url }})<br>
>{{ edu.details }}
{% endfor %}

## Teaching
{% for teaching in load_data('teaching.yaml')['teachings'] %}
### {{ teaching.course }}
*{{ teaching.position }}, {{ teaching.institution }}, {{ teaching.period }}*<br>
>{{ teaching.details }}<br>
{% endfor %}