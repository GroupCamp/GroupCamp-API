
[The known types](./README.md)

[Main page](../README.md)

# ProjectInReport type definition

Name    |   Type  |  Description
--------|---------|-------------
group_id | Uuid | Group UUID
name | String | Project name. Can contain the Project Code, if applicable.
group_name | String | Raw group name, without Project Code.
state | Enum(archi, ok, del, trash) | Current group status.
leader1 | [SimpleUser](../types/SimpleUser.md) | Project leader 1 (The user must be a project manager).
leader2 | [SimpleUser](../types/SimpleUser.md) | Project leader 2 (Assistant, the user must be a project manager).
rich_tags | Array([STag](../types/STag.md)) | Group's tags
tags_names | Array(String) | Group's tags names


