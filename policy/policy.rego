package authorization

default allow = false

allow {
    input.role == "admin"
}

allow {
    input.role == "user"
    input.action == "read"
}
