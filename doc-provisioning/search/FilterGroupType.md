
[The known type-based filters](./README.md)

[Main page](../README.md)

# The definition of type-based filter FilterGroupType

A filter is composed of a base and some types to be added or removed.

A filter like **Empty,type1,type2** will match only objects having type type1 or type2.

A filter like **All,!type1** will match objects having any type except type1.

In the two previous examples **All** and **Empty** are bases and **type1** and **type2** are elements.

### Declared bases for FilterGroupType

Name     |  Description 
---------|--------------
All | The 'All' base contains all types for the filter
Empty | The 'Empty' base contains no preset elements
Multi | The 'Multi' base contains all the type of groups which can appear multiple times in a given account


### Declared elements for FilterGroupType

Name    |   Description
--------|---------------
project  |  Type 'project'



