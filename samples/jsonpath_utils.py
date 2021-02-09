
import jsonpath

d1={"access_token":"42_gaFxKzOPgYYIrMblk6yO1tuzOi7dV9cYEwIVpRY8jGThYRkRpIwSpcoHwm3CF7r9YuUwJWm9tDbpsW3gqsGOVm7bHDhV2MB-QcB0UHGXQOXLRHQ78tBUJNg6mcGCylk9HZNkxi3lOXTCqB1vZAWjAIAGHD","expires_in":7200}
print(d1["access_token"])
print(jsonpath.jsonpath(d1,'$.access_token')[0])

d2={"tags":
[{"id": 1,"name": "每天一罐可乐星人","count": 0},
    { "id": 2,"name": "星标组","count": 0},
    {"id": 127,"name": "广东","count": 5}
  ]
}

#方如bejson
print(d2["tags"][1]["name"])
print(jsonpath.jsonpath(d2,'$.tags[1].name')[0])