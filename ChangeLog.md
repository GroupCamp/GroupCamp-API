# GroupCamp API Release notes

2018-09-25 - Managing organizations (Companies)

* Published the API to create, get, edit and list invited organizations (aka
  "Companies" in the GroupCamp web interface).
* `orga` and `subtype` fields can be set when creating/editing a project. When
  the subtype is `customer` (for customer's projects), the `orga` field allows
  to choose the customer's company.
* Example of code has been added to the `orga.py` script.

2018-09-25 - Tag management for projects
* Fields `rich_tags` (tag's uuid, name, color and where it may be used) and
  `tag_names` (only the names) are added to the informations returned to
  describe a project.
* The field `tag_names` can be used to change/set the tags of a project when
  creating or editing.
* New `STag` type definition
* Example of tag management code has been added to the `group.py` script.

