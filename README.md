# circleci-python-dockerfile

Dockerfiles for CircleCI's Docker images.

## Flavours

All versions (tags) include `libhdf5-dev` library and are ready in three flavours:

 * `plain` - python installed via pyenv with some additional options and flags,
 * `psqlclient` - `shared` + PostgreSQL client,
