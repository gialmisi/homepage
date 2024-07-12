---
hide:
 - navigation
---
# Activities and Rewards
## Positions
{% for position in load_data('activities.yaml')['positions'] %}
### {{ position.position }}
{{ position.organization }}, {{ position.period }}{% if position.details %}
>{{ position.details }}{% endif %}
{% endfor %}

## Rewards and Nominations
{% for reward in load_data('activities.yaml')['rewards'] %}
### {{ reward.name }}
{{ reward.organization }}, {{ reward.date }}<br>
>{{ reward.details }}
{% endfor %}

## Grants
{% for funding in load_data('activities.yaml')['fundings'] %}
### {{ funding.name }}
{{ funding.organization }}, {{ funding.date }}<br>
>{{ funding.details }}
{% endfor %}
