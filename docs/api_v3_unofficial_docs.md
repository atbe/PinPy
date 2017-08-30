# Unofficial Documentaion on Pinterest v3 api

> Some of the Parameters are used for multiple sub-endpoints and some are not used at all on some sub-endpoints. Mix and match to see what has an effect and what doesn't (or just think about it and if the parameter doesn't make sense it probably won't be used).
I won't be checking each and every sub-endpoint to see which parameters it accepts. Maybe in the future (or someone else can do it).

### /boards - **Authorization required.**
`https://api.pinterest.com/v3/boards/{board_id}/`

Parameters:

- `access_token`: **Required** used to authenticate request.
- `page_size`: Number of results to return. **MAX = 250**
- `bookmark`: Optional, used for pagination if results (from sub-endpoints) exceed page_size.
-

Sub-endpoints:

- `/pins` - Returns the Pins on the given board.
- `/followers` - Returns all the followers of this board.
- `/collaborators` - Returns all the collaborators of this board.

### /pins - **Authorization required.**
`https://api.pinterest.com/v3/pins/{pin_id}/`

Parameters:

- `access_token`: **Required** used to authenticate request.
- `page_size`: Number of results to return. **MAX = 250**
- `bookmark`: Optional, used for pagination if results (from sub-endpoints) exceed page_size.

Sub-endpoints:

- `/likes` - Returns the users who have liked this Pin.
- `/comments` - Returns all of the comments made on a Pin.

### /users - **Authorization required.**
`https://api.pinterest.com/v3/users/{user_id}/`

Parameters:

- `access_token`: **Required** used to authenticate request.
- `page_size`: Number of results to return. **MAX = 250**
- `bookmark`: Optional, used for pagination if results (from sub-endpoints) exceed page_size.

Sub-endpoints:

- `/followers` - Returns the users who are following this user.
- `/following` - Returns the users this user is following.
- `/boards` - Returns the users boards.
- `/pins` - Returns the users pins.
- `/comments` - Returns all of the comments made on a Pin.
