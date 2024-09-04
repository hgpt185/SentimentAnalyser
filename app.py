import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'],'/slack/events', app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']

@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    print(text)

    if 'analyse-call' in text:
        client.chat_postMessage(channel=channel_id, text="text")

    elif 'analyse-team' in text:
        client.chat_postMessage(channel=channel_id, text="text2")
    
    elif 'analyse-products' in text:
        client.chat_postMessage(channel=channel_id, text="text3")

    else:
        client.chat_postMessage(channel=channel_id, text="Invalid command!")

    # if user_id != BOT_ID:
    #     client.chat_postMessage(channel=channel_id, text=text)

block_content = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":wave: *Hey Jennifer*"
			}
		},
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Your Team's Calls Sentiment",
				"emoji": True
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Emma - Highly Positive :heart_eyes:*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Oliver - Mostly Negative :rage:*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*William - Neutral :no_mouth:*"
			}
		},
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": ":muscle: Great job on driving positive customer sentiment",
				"emoji": True
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Emma said:* _\"With Sales Cloud you can track and monitor every customer's sales journey from start to finish in one place. You can use automation and sales management tools to sell more efficiently so you can focus on delivering a great customer experience and closing deals. A single view of each customer means your team can focus on the deal, not the record keeping. You will securely access and share information wherever, whenever, with the Salesforce Mobile app. In addition, you can easily set up and access real-time reports so you're always up-to-date with what's happening. Moreover, a company-wide pipeline visibility shows top performing teams and individuals. You can make your workflow smarter by connecting your apps to Salesforce. Last, you can discover over 3,000 apps that extend the power of Salesforce at the Salesforce AppExchange.\"_"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Customer responded:* _\"Wow, that sounds really interesting, and it was under two minutes like promised!\"_"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Listen",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0",
					"style": "primary",
					"url": "https://google.com"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Share"
					},
					"style": "primary",
					"value": "Share"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Give Kudos :celebrate:"
					},
					"style": "primary",
					"value": "Give Kudos"
				}
			]
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Emma said:* _\"I think so. Will you allow me to give it a try?\"_"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Customer responded:* _\"Sure, go for it!\"_"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Listen",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0",
					"style": "primary",
					"url": "https://google.com"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Share"
					},
					"style": "primary",
					"value": "Share"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Give Kudos :celebrate:"
					},
					"style": "primary",
					"value": "Give Kudos"
				}
			]
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Emma said:* _\"Great, I'm sending you an invite\"_"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Customer responded:* _\"Thank you, it's been great speaking with you!\"_"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Listen",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0",
					"style": "primary",
					"url": "https://google.com"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Share"
					},
					"style": "primary",
					"value": "Share"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Give Kudos :celebrate:"
					},
					"style": "primary",
					"value": "Give Kudos"
				}
			]
		},
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": ":v: Try these options to avoid using negative sentiment",
				"emoji": True
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Emma said:* _\"Don't have much time either so please hurry up!\"_"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Listen",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0",
					"style": "primary",
					"url": "https://google.com"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Share"
					},
					"style": "primary",
					"value": "Share"
				}
			]
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Rephrase:* _\"Y\"_"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Oliver said:* _\"You know I told you that this offer will not be on the table forever\"_"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Listen",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0",
					"style": "primary",
					"url": "https://google.com"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Share"
					},
					"style": "primary",
					"value": "Share"
				}
			]
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Rephrase:* _\"X\"_"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Oliver said:* _\"I really put myself on the line for you to get this discount, you could have made the effort\"_"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Listen",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0",
					"style": "primary",
					"url": "https://google.com"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Share"
					},
					"style": "primary",
					"value": "Share"
				}
			]
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Rephrase*: _\"Y\"_"
			}
		},
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": ":raised_hands: Handle negative customer feedback more effectively",
				"emoji": True
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Customer said:* _\"Before our next meeting, can you prepare an overview of your competitors? Not sure why I should choose this product over others out there and I didn't feel you've addressed this at all. Looks like you're also in a hurry. Not just me.\"_"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Emma responded:* _\"That's not True! I'm not in a hurry. You mentioned you only have 2 minutes. I'll prepare such an overview for our next meeting if you insist. When would be a convenient time for you?\"_"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Listen",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0",
					"style": "primary",
					"url": "https://google.com"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Share"
					},
					"style": "primary",
					"value": "Share"
				}
			]
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Rephrase:* _\"Z\"_"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Customer said:* _\"Not so good, really busy times over here. Not a good time for this call either.\"_"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Oliver responded:* _\"It's never a good time, so let's talk now. I am calling to ask about the price quote I sent you. Did you review the new discounted proposal I sent you?\"_"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Listen",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0",
					"style": "primary",
					"url": "https://google.com"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Share"
					},
					"style": "primary",
					"value": "Share"
				}
			]
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Rephrase:* _\"Z\"_"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Customer said:* _\"I can't promise you that, or anything. I'm also not really liking the pushy nature of this call. To be honest one of your competitors gave us a better offer\"_"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Oliver responded:* _\"Really? What did they offer you?\"_"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Listen",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0",
					"style": "primary",
					"url": "https://google.com"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Share"
					},
					"style": "primary",
					"value": "Share"
				}
			]
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Rephrase:* _\"Z\"_"
			}
		},
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": ":speech_balloon: More Suggestions",
				"emoji": True
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Consider reaching out to Oliver and William and sharing with them some of the examples mentioned here. Maybe Emma can help coach the other reps on the team."
			}
		}
	]
    

@app.route('/slack/message-count', methods=['POST'])
def message_count():
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get('channel_id')

    message_payload = {
        "channel": channel_id,
	    "blocks": block_content
        }

    try:
        client.chat_postMessage(**message_payload)
    except slack.errors.SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")

    return Response(), 200

if __name__ == "__main__":
    app.run(debug=True)