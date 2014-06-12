import unirest
import json

def summarize(input_text):
  response = unirest.post("https://textteaser.p.mashape.com/api",
    headers={
      "X-Mashape-Authorization": "zwpVdAzvllLnWrknIH5SacoYvPGD0VNJ"
    },
    params={ 
      "text": input_text,
      "title": "Football info",
      # "url": "<url>",
      # "category": "[\"Technology\",\"Sports\",\"Entertainment\",\"etc.\"]",
      # "blog": "[\"TechCrunch\",\"The Verge\",\"Mashable\",\"Business Insider\",\"etc.\"]"
    }
  );

  return ' '.join(json.loads(response.raw_body)['sentences'])

TEXT = """Macbeth (full title The Tragedy of Macbeth) is a tragedy written by William Shakespeare, and is considered one of his darkest and most powerful works. Set in Scotland, the play dramatizes the corrosive psychological and political effects produced when evil is chosen as a way to fulfil the ambition for power.

The play is believed to have been written between 1599 and 1606, and is most commonly dated 1606. The earliest account of a performance of what was probably Shakespeare's play is the Summer of 1606, when Simon Forman recorded seeing such a play at the Globe Theatre.[1] It was first published in the Folio of 1623, possibly from a prompt book. It was most likely written during the reign of James I, who had been James VI of Scotland before he succeeded to the English throne in 1603. James was a patron of Shakespeare's acting company, and of all the plays Shakespeare wrote during James's reign, Macbeth most clearly reflects the playwright's relationship with the sovereign.

Macbeth is Shakespeare's shortest tragedy, and tells the story of a brave Scottish general named Macbeth who receives a prophecy from a trio of witches that one day he will become King of Scotland. Consumed by ambition and spurred to action by his wife, Macbeth murders King Duncan and takes the throne for himself. He is then wracked with guilt and paranoia, and he soon becomes a tyrannical ruler as he is forced to commit more and more murders to protect himself from enmity and suspicion. The bloodbath and consequent civil war swiftly take Macbeth and Lady Macbeth into the realms of arrogance, madness, and death.

Shakespeare's source for the tragedy is the account of King Macbeth of Scotland, Macduff, and Duncan in Holinshed's Chronicles (1587), a history of England, Scotland and Ireland familiar to Shakespeare and his contemporaries, although the events in the play differ extensively from the history of the real Macbeth. In recent scholarship, the events of the tragedy are usually associated more closely with the execution of Henry Garnett for complicity in the Gunpowder Plot of 1605.[2]

In the backstage world of theatre, some believe that the play is cursed, and will not mention its title aloud, referring to it instead as "the Scottish play". Over the course of many centuries, the play has attracted some of the most renowned actors to the roles of Macbeth and Lady Macbeth. It has been adapted to film, television, opera, novels, comic books, and other media.
"""

if __name__ == '__main__':
  print summarize(TEXT)