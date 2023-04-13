# Siphon Vbot extension
- `140` commands
- `7` categories

## How to setup:
- Download Python
- Run `install.py`
- Run `main.py`

## Added features:

### Fun

| Command | Description |
|:---------:|:-------------:|
| `animate <text>` | Animates the given text. |
| `animate extend <text>` | Extends the current animation with the given text. |
| `animate shift <shift> <steps> <text>` | Shifts the animation by the given amount and steps, and then adds the given text. |
| `animate custom` | Opens a prompt to enter a custom animation. |
| `animate custom <animation>` | Uses the given animation to animate the text. |
| `ghostping <user>` | Pings and instantly deletes the given user's message in all channels. |
| `wasted <user>` | Overlays the wasted meme onto the given user's avatar. |
| `cock <user>` | Gives a description of the given user's cock. |
| `slotmachine` | Depicts a slot machine and determines if you won the jackpot, just won or lost. |
| `coinflip` | Flips a coin. |
| `wyr {option1} or {option2}` | Asks a "would you rather" question with the given options. |
| `twerk <user>` | Twerks on the given user. |
| `gaymeter <user>` | Determines how gay the given user is. |
| `empty` | Sends an empty message. |

### Utility
| Command | Description |
|:---------:|:-------------:|
| `random number <low> <high>` | Generates a random number between the given low and high values. |
| `random color` | Generates a random color. |
| `random mention [<str>]` | Mentions a random user with an optional string as a filter. |
| `fakeinfo` | Generates some fake info. |
| `qrcode <url>` | Creates a QR code for the given URL. |
| `resolve <domain>` | Resolves the given domain name. |
| `remote <channel> <message>` | Sends a message in another channel or server. |
| `sendasfile <name> <content>` | Sends a file with the given name, extension, and contents. |
| `stealnick <user>` | Sets your nickname to the given user's nickname. |
| `bio <text>` | Sets your bio to the given text. |
| `scrape <amount> <filename>` | Scrapes the channel for the specified amount of messages and exports it to a file |

### Text  
| Command | Description |
|:---------:|:-------------:|
| `fancy <text>` | Makes the given text fancy. |
| `cursed <text>` | Makes the given text cursed. |
| `translate <language> <text>` | Translates the given text into the given language. |
| `morsecode <text>` | Translates the given text into morse code. |
| `editglitch <text>` | Does the Discord edited glitch on the given text. |
| `emojisep <emoji> <text>` | Separates the given text with the given emoji instead of spaces. |
| `regional <text>` | Sends a message using regional indicators. |
| `emojireact <message link> <text>` | reacts to a message with letters and numbers (no repeat characters) |

### Misc

| Command       | Description                                   |
|:---------:|:-------------:|
| calc `<string>`  | Calculates a string like a calculator          |
| mcstatus `<server>` | Gets the status of a Minecraft server            |
| poll `<question>` | Sends a poll                                    |
| chessboard `<FEN>` | Creates an image of a chess board with a FEN string |
| placeholder `<string>` | Replaces certain placeholders            |
| adlinkbypass `<link>` | Bypasses Linkvertise and other ad links           |


### Raiding

| Command       | Description                                   |
|:---------:|:-------------:|
| token get        | Retrieves your user token                     |
| token info `<token>` | Gets information about a user token               |
| chessploit email `<email>` | Gets the username associated with an email address |
| chessploit username `<username>` | Gets the email address associated with a username |
| pingall        | Pings everyone in the server without @everyone perms |

### Non-command Features
 - CONFIG: toggle error logging (toggle on or off error logging and where the errors will appear)
 - CONFIG: toggle timestamps in console messages (toggle timestamps on errors and commands sent)
 - changed formatting of certain console messages


### Improvements
 - added optional pause value to `spam` module
 - fixed unclosed connection error in the `spam fast` command
 - automatic token input from `install.py`
 - Fixed colors not show properly in default windows command prompt when loading cogs
 - Fixed firstmsg command and made it better

## Note:
I did not create this with the intention to copy or steal [vined_](https://github.com/vined-underscore/VBot)'s work by extending his bot. I merely wished to add some new functionality while still being able to publish it to github. It does not go against the original Vbot license as the GNU license states that I can do pretty much anything with the source code apart from distributing a close sourced application that includes some of the code.