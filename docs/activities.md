---
hide:
 - navigation
---
# Activities
## Positions
{% for position in load_data('activities.yaml')['positions'] %}
### {{ position.position }}
{{ position.organization }}, {{ position.period }}{% if position.details %}
>{{ position.details }}{% endif %}
{% endfor %}

## Rewards
{% for reward in load_data('activities.yaml')['rewards'] %}
### {{ reward.name }}
{{ reward.date }}, {{ reward.organization }}<br>
>{{ reward.details }}
{% endfor %}

