## Actions

| Command                                          | Description                                                                                     |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `.add <i>pickup</i>[ <i>pickup</i> ..]] or +<u>pickup</u>[ <i>pickup</i> ..]]` | Adds you to specified pickups.                                                                |
| `.add or ++`                                     | Adds you to all active pickups.                                                               |
| `.remove <i>pickup</i>[ <i>pickup</i> ...] or -[<i>pickup</i>[ <i>pickup</i> ..]]`  | Removes you from specified pickups.                                                           |
| `.remove or --`                                 | Removes you from all pickups.                                                                  |
| `.expire <i>time</i>`                                     | Sets new time delay after you will be removed from all pickups, example: '.expire 1h 2m 3s'. |
| `.default_expire <i>time</i>`, 'afk' or 'none'   | Set your personal default .expire time or set autoremove on afk status.                         |
| `.sub`                                           | Request sub for last game.                                                                     |
| `.allowoffline or .ao`                          | Gives you immunity from getting removed by offline or afk statuses until a pickup with you starts. (done for mobile devices users). |
| `.subscribe <i>pickup</i>[ <i>pickup</i> ..]]`  | Adds the promotion role of specified pickup(s) to you.                                         |
| `.unsubscribe <i>pickup</i>[ <i>pickup</i> ..]]` | Removes the promotion role of specified pickup(s) from you.                                    |

## Info

| Command                                          | Description                                                                                     |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `.who [<i>pickup</i>[ <i>pickup</i> ...]]`       | List of users added to a pickups.                                                             |
| `.pickups`                                       | List of all pickups on the channel.                                                            |
| `.pickup_groups`                                | List of pickup groups configured on the channel.                                               |
| `.expire`                                       | Shows you how much time left before you will be removed from all pickups.                       |
| `.lastgame [<i>@nick</i> or <i>pickup</i>]`     | Show last pickup, or last pickup by specified argument.                                         |
| `.liast [void or mode]`                         | Show last pickup and list of current players in.                                                |
| `.top [pickup] [weekly or monthly or yearly]`   | Shows you most active players.                                                                 |
| `.top [<i>pickup</i>] [weekly or monthly or yearly]` | Shows you most active players.                                                               |
| `.stats [<i>nick</i> or <i>pickup</i>]`         | Shows you overall stats or stats for specified argument.                                        |
| `.ip [<i>pickup</i> or default]`                | Shows you ip of last pickup or specified pickup.                                                |
| `.map <i>pickup</i>`                            | Print a random map for specified pickup.                                                        |
| `.maps <i>pickup</i>`                           | Show all maps for specified pickup.                                                             |

## Picking Teams

| Command                                          | Description                                                                                     |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `.cointoss or .ct [heads or tails]`             | Toss a coin.                                                                                    |
| `.pick <i>@nick</i>`                            | Pick a user to your team.                                                                       |
| `.put <i>@nick</i> alpha or beta`               | Put player in specified team (available only for users with moderator or admin rights).          |
| `.subfor <i>@nick</i>`                          | Become a substitute for specified player.                                                        |
| `.capfor alpha or beta`                         | Become a captain of specified team.                                                             |
| `.teams`                                        | Show teams for current pickup.                                                                  |

## Ranking

| Command                                          | Description                                                                                     |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `.leaderboard [page] or .lb [page]`             | Show top players by rating.                                                                     |
| `.rank`                                         | Show your rating stats.                                                                         |
| `.reportlose or .rl`                            | Report loss on your current match (available for captains only).                                 |
| `.reportdraw .draw or .rd`                      | Report draw on your current match (available for captains only, captain of other team has to confirm). |
| `.reportcancel or .rc`                          | Report cancel on your current match (available for captains only, captain of other team has to confirm). |
| `.matches`                                      | Show all active matches on the channel.                                                         |
| `.ranks_table`                                  | Show rank to rating table.                                                                      |

## For moderators and above

| Command                                          | Description                                                                                     |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `.reportwin or .rw <i>match_id</i> alpha or beta` | Report win on specified match for specified team.                                              |
| `.undo_ranks <i>match_id</i>`                   | Undo all rating changes for a previously reported match.                                         |
| `.seed <i>@nick</i> <i>rating</i>`              | Set specified player's rating points, also this will disable initial rating calibration for this user. |
| `.reset_ranks`                                  | Reset all rating data on the channel. Warning, this action is irreversible!                      |

## For admins

| Command                                          | Description                                                                                     |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `.reset_ranks`                                  | Reset all rating data on the channel. Warning, this action is irreversible!                      |

## Moderation

| Command                                          | Description                                                                                     |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `.noadd <i>@nick</i> [<i>time</i>] [<i>reason</i>]` | Disallow user to play pickups.                                                               |
| `.noadds`                                       | Show list of users who are disallowed to play pickups.                                          |
| `.forgive <i>@nick</i>`                         | Allow user from noadds list to play pickups.                                                    |
| `.phrase <i>@nick</i> <i>text</i>`             | Set specified reply for specified user after .add command.                                       |
| `.remove_player <i>@nick</i>`                   | Remove specified players from all pickups.                                                      |
| `.reset`                                        | Removes all players from all pickups.                                                            |
| `.start <i>pickup</i>`                          | Force a pickup to start with deficient players count.                                            |
| `.cancel_match <i>match_id</i>`                 | Cancel an active match, match_id can be found at the beginning of pickup start message.           |

## Configuration

| Command                                          | Description                                                                                     |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `.enable_pickups`                               | Turn on the pickup bot on the channel.                                                          |
| `.disable_pickups`                              | Turn off the bot and delete all configurations/stats on the channel. Warning, this action is irreversible! |
| `.add_pickups <i>name</i>:<i>players</i>[ <i>name</i>:<i>players</i> ...]` | Create new pickups.                                                                       |
| `.remove_pickups <i>pickup</i>[ <i>pickup</i> ...]` | Delete specified pickups.                                                                   |
| `.add_pickup_group <i>group_name</i> <i>pickup</i>[ <i>pickup</i>...]` | Create a pickup group which will contain specified pickups.                                  |
| `.remove_pickup_group <i>group_name</i>`        | Delete specified pickup group.                                                                 |
| `.reset_stats`                                  | Delete all channel statistics.                                                                  |
| `.cfg`                                          | Show global channel configuration variables.                                                     |
| `.pickup_cfg <i>pickup</i>`                      | Show specified pickup configuration variables.                                                  |
| `.set_ao_for_all <i>name</i> 0 or 1`               | Allow/disallow offline for all users of specific pickup kind.                                    |
| `.set_default variable value`                   | Set a global variable value. Availible variables: admin_role, moderator_role, captains_role, prefix, default_bantime, ++_req_players, startmsg, submsg, ip, password, maps, pick_captains, pick_teams, promotion_role, promotion_delay, blacklist_role, whitelist_role, require_ready, ranked, ranked_calibrate, ranked_multiplayer, help_answer. |
| `.set_pickups <i>pickup</i>[ <i>pickup</i>...] variable value` | Set variables for specified pickups. Availible variables: maxplayers, startmsg, submsg, ip, password, maps, pick_captains, pick_teams, pick_order, promotion_role, blacklist_role, whitelist_role, captains_role, require_ready, ranked, help_answer. |

### Configuration Variables

* For any variable set 'none' value to disable.
* admin_role <i>role_name</i> - Users with this role will have access to configuration and moderation commands.
* moderator_role <i>role_name</i> - Users with this role will have access to moderation commands.
* captains_role <i>role_name</i> - Random captains will be preferred to this role, also '.capfor' command will be only available for users with this role if it's set.
* prefix <i>symbol</i> - Set prefix before all bot's commands, default '.'.
* default_bantime <i>time</i> - Set default time for .noadd command.
* ++_req_players <i>number</i> - Set minimum pickup required players amount for '++' command or '.add' command without argument, so users won't add to 1v1/2v2 pickups unintentionally. Default value: 5.
* startmsg <i>text</i> - Set message on a pickup start. Use %ip% and %password% in <i>text</i> to represent IP and password.
* start_pm_msg <i>text</i> - Set private message on a pickup start. Use %pickup_name%, %ip%, %password%, and %channel% to represent its values.
* submsg <i>text</i> - Set message on .sub command. Use %pickup_name%, %ip%, %password%, and %promotion_role% to represent its values.
* promotemsg <i>text</i> - Set message on .promote command. Use %promotion_role%, %pickup_name%, and %required_players% to represent its values.
* ip <i>text</i> - Set IP which will be shown in startmsg, submsg, and on .ip command.
* password <i>text</i> - Set password which will be shown in startmsg, submsg, and on .ip command.
* maps <i>map_name</i>[, <i>map_name</i>...] - Set maps.
* pick_captains 0, 1, 2, or 3 - Set if the bot should suggest captains.
  * If the variable ranked is 0:
    * 0 - Doesn't suggest captains
    * 1 - Picks captains randomly but with a preference for players having the captain role
    * 2 - Picks captains randomly
  * If the variable ranked is 1:
    * 0 - Doesn't suggest captains
    * 1 - Sorts players by player having captain role and player rank and picks two players from the top
    * 2 - Sorts players by player rank and picks a random pair of adjacent players
    * 3 - Picks captains randomly
* pick_teams <i>value</i> - Set teams pick system the bot should use. Value must be in 'no_teams', 'auto', or 'manual'.
  * no_teams - Bot will only print players list and captains if needed.
  * auto - Bot will print teams balanced by rating on ranked pickups or random teams.
  * manual - Users will have to pick teams using teams picking commands.
* team_emojis <i>emoji</i> <i>emoji</i> - Set custom team emojis.
* team_names <i>alpha_name</i> <i>beta_name</i> - Set custom team names (commands with team names will change accordingly).
* pick_order <i>order</i> - Force specified teams picking order. Example value: 'abababba'.
* promotion_role <i>role_name</i> - Set promotion_role to highlight on .promote and .sub commands.
* promotion_delay <i>time</i> - Set time delay between .promote and .sub commands can be used.
* blacklist_role <i>role_name</i> - Users with this role will not be able to add to specified pickups.
* whitelist_role <i>role_name</i> - Only users with this role will be able to add to specified pickups.
* require_ready none or <i>time</i> - If set, users will have to confirm themselves using '.ready' command.
* ranked 0 or 1 - Set pickup(s) to have a rating system and make players have to report their matches.
* ranked_calibrate 0 or 1 - Set to enable rating boost on the first 10 user's matches, default on. Only for 'set_default'.
* ranked_multiplayer 8 to 256 - Change rating K-factor (gain/loss multiplier), default 32. Only for 'set_default'.
* ranked_streaks 1 or 0 - Set to enable ranked streaks (starting from x1.5 for (3 wins/loses in a row) to x3.0 (6+ wins/loses in a row)).
* initial_rating <i>integer</i> - Set starting rating for new players (default is 1400).
* global_expire <i>time</i>, afk, or none - Set default_expire value for users without personal settings.
* match_livetime <i>time</i> - Set a time limit before a match gets aborted as timed out.
* help_answer <i>text</i> - Set an answer on .help command.
