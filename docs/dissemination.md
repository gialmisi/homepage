---
hide:
 - navigation
---
# Dissemination

## Conferences
{% for conference in load_data('disseminations.yaml')['conferences'] %}
### {{ conference.title }}
*{{ conference.event }}, {{ conference.date }}*<br>
{% if conference.slides %}[Slides]({{ conference.slides }}){% endif %}{% if conference.recording %}{% if conference.slides %} | {% endif %}[Recording]({{ conference.recording }})
{% endif %}
{% endfor %}

## Invitations
{% for invitation in load_data('disseminations.yaml')['invitations'] %}
### {{ invitation.title }}
*{{ invitation.event }}, {{ invitation.date }}*<br>
{% if invitation.slides %}[Slides]({{ invitation.slides }}){% endif %}{% if invitation.recording %}{% if invitation.slides %} | {% endif %}[Recording]({{ invitation.recording }})
{% endif %}
{% endfor %}

## Presentations
{% for presentation in load_data('disseminations.yaml')['presentations'] %}
### {{ presentation.title }}
*{{ presentation.event }}, {{ presentation.date }}*<br>
{% if presentation.slides %}[Slides]({{ presentation.slides }}){% endif %}{% if presentation.recording %}{% if presentation.slides %} | {% endif %}[Recording]({{ presentation.recording }})
{% endif %}
{% endfor %}

## Tutorials
{% for tutorial in load_data('disseminations.yaml')['tutorials'] %}
### {{ tutorial.title }}
*{{ tutorial.event }}, {{ tutorial.date }}*<br>
{% if tutorial.slides %}[Slides]({{ tutorial.slides }}){% endif %}{% if tutorial.recording %}{% if tutorial.slides %} | {% endif %}[Recording]({{ tutorial.recording }})
{% endif %}
{% endfor %}

## Posters
{% for poster in load_data('disseminations.yaml')['posters'] %}
### {{ poster.title }}
*{{ poster.event }}, {{ poster.date }}*<br>
{% if poster.poster %}[Poster]({{ poster.poster }})
{% endif %}
{% endfor %}