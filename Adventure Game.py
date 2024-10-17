def makeGame():
    game = {
      "start": ["You were trying to cash in a check at the bank, when you hear shouting by the entrance.", "Stay put", "stay", "Check what's going on", "check"], 
      "stay": ["You stay at the kiosk. Three robbers then enter the lobby, shoot all the guards and make everyone get on their knees.", "Comply", "comply", "Try to fight them", "resist"], 
      "check": ["You surprise one of the robbers and get shot right in the face. You are dead. [SURPRISE!!! ENDING]", "Start over", "retry", "Quit", "quit"], 
      "comply": ["You get on your knees and stay in place. The robbers spread out through the bank - leaving the front door unguarded.", "Run to the door", "run", "Stay in place", "freeze"], 
      "resist": ["You get ready to fight, but get shot 3 times in the chest. You are still alive but barely.", "Try to get up", "try", "Stay down", "lie"], 
      "run": ["You make it to the front door, but get shot in the leg. You can still make it out.", "Run out", "flee", "Fall to the ground", "fall"], 
      "freeze": ["You stay on your knees. 2 of the robbers leave to get to the bank vault, leaving one behind. His back is towards you.", "Sneak up behind him", "sneak", "Stay in place", "halt"], 
      "try": ["You slowly get up to your feet, but get shot again - this time in the head. You are dead. [FAILED HERO ENDING]", "Start over", "retry", "Quit", "quit"], 
      "lie": ["You stay on the ground. One of the robbers comes over to check if you're really dead. His grasp on his gun is loose.", "Steal the robber's gun", "steal", "Stay on the ground", "wait"], 
      "flee": ["You push through the door to the outside. A payphone is to your left, but your car is to your right.", "Go to the payphone", "payphone", "Run to the car", "car"], 
      "fall": ["You fall to the ground. Two of the robbers rush over and shoot you more. You are dead. [NO ESCAPE ENDING]", "Start over", "retry", "Quit", "quit"], 
      "sneak": ["You get off your knees and sneak up behind him. he doesn't notice you.", "Knock the robber out", "knock", "Take the robber's gun", "take"], 
      "halt": ["You stay on the ground. The 2 robbers return from the vault with bags of cash. They're making a move towards the door.", "Block off the entrance", "block", "Stay down on the ground", "choke"], 
      "steal": ["You take the robber's gun and hold him at gun point. He surrenders. What do you do with him now?", "Kill the robber", "execute", "Hold him hostage", "spare"], 
      "wait": ["You stay on the ground. The robber shoots you in the head twice to make sure you're dead. You are dead. [DOUBLE TAP ENDING]", "Start over", "retry", "Quit", "quit"], 
      "payphone": ["You limp over to the payphone and contact the police. They tell you they'll get to the scene in 5 minutes. The robbers will run in that time.", "Block off the bank door", "barricade", "Run away", "scurry"], 
      "car": ["You limp over to your car. You get in the front seat and start it up. You can go to the police station, or you can wait.", "Go to the police station", "police", "Wait on the curb", "sit"], 
      "knock": ["You knock the robber unconcious. The other two haven't left the vault yet.", "Go to the vault", "vault", "Take the robber's gun", "arm"], 
      "take": ["You try to take the robber's gun. He notices and knocks you out. You wake up hours later and the bank is empty. The hostages have been freed and the money has been stolen. The robbers won. [GOOD TRY ENDING]", "Start over", "retry", "Quit", "quit"], 
      "block": ["You block off the entrance to the bank. The robbers shoot you down and escape. The robbers won. [HEROIC NONSENSE ENDING]", "Start over", "retry", "Quit", "quit"], 
      "choke": ["You stay on the ground. The robbers leave the bank with all the money. The robbers won. [INACTION ENDING]", "Start over", "retry", "Quit", "quit"], 
      "execute": ["You gun down the robber and kill him. The other two haven't left the vault yet.", "Go to the vault", "continue", "Kill the hostages", "kill"], 
      "spare": ["You knock out the robber and tie him up using his belt. The other two robbers come back from the vault. One has a pistol in their hand. The other has two large bags of money in their hands.", "Shoot the robber with the gun", "gun", "Shoot the robber with the money", "money"], 
      "barricade": ["You block off the entrance to the bank with a thick piece of wood you found in the alley. The police arrive and arrest the robbers, while you go to the hospital to treat your wound. You won. [INJURED ENDING]", "Start over", "retry", "Quit", "quit"], 
      "scurry": ["You limp away from the payphone and keep going. The robbers run away with the money, while you run away to skip town. The robbers won. [COWARD ENDING]", "Start over", "retry", "Quit", "quit"], 
      "police": ["You drive to the police station. You tell the cops there what's going on, and they follow you back to the bank. The robbers were about to cross the street when you and the police stop them. You won. [LAW INVOLVMENT ENDING]", "Start over", "retry", "Quit", "quit"], 
      "sit": ["You wait on the curb. The robbers exit the back and get into your car, before you drive off. You were the robber's getaway driver - acting as a civilian in disguise so you could help them on their heist. You won? [PLOT TWIST ENDING]", "Start over", "retry", "Quit", "quit"], 
      "vault": ["You go the vault. The two robbers are still trying to break into it. They haven't noticed you.", "Sneak up behind the robbers", "stealth", "Make yourself known", "announce"], 
      "arm": ["You take the robber's gun. The other two robbers come back from the vault. You try to shoot the robber's but you accidentally turned the safety on. The robbers gun you down in response. You are dead. [BAD GUN OWNER ENDING]", "Start over", "retry", "Quit", "quit"], 
      "continue": ["You go to the bank's vault. The robbers are still there. Both are tyring to open the door.", "Kill both the robbers", "double kill", "Kill one of the robbers", "shoot"], 
      "kill": ["You kill everyone in the bank lobby. The robbers return from the vault with money in their hands. You kill them too. One of the hostages called the police, and they're on their way.", "Leave the bank", "leave", "Stay in the bank", "remain"], 
      "gunman": ["You shoot the robber with the gun. He falls to the ground dead. The other throws the bags away and surrender. The police arrive and arrest the last robber. You won. [STOPPED THE ROBBERY ENDING]", "Start over", "retry", "Quit", "quit"], 
      "money": ["You shoot the robber with the money bags. He falls to the ground dead, the other robber shoots you. You are dead. [LAST STAND ENDING]", "Start over", "retry", "Quit", "quit"], 
      "stealth": ["You sneak up behind the robbers. You take both of the robber's guns from their holsters. You hold them both at gun point and they surrender. The police arrive and arrest the criminals. You won. [STEALTH 100 ENDING]", "Start over", "retry", "Quit", "quit"], 
      "announce": ["You shout at the robbers. They turn around to face you and unholster their guns. They then shoot you down. You are dead. [LOUD AND PROUD ENDING]", "Start over", "retry", "Quit", "quit"], 
      "double kill": ["You kill both the robbers. They've managed to open the bank vault. The bank currently holds 500 million in cash.", "Take the cash", "rob", "Head back to the lobby", "return"], 
      "shoot": ["You kill one of the robbers. The other notices you and shoots you dead. You are dead. [SO CLOSE YET SO FAR ENDING]", "Start over", "retry", "Quit", "quit"], 
      "leave": ["You leave the bank. The robbery makes local news. The robbers got blamed for the murders. The police don't suspect you in the slightest. You won... you monster. [GOT AWAY WITH IT ENDING]", "Start over", "retry", "Quit", "quit"], 
      "remain": ["You stay in the bank. The police arrive and arrest you. You've been charged with mass murder, and expected to go to jail for life - with no parole and potential plans for the death penelty. You won? [MURDERER ENDING]", "Start over", "retry", "Quit", "quit"], 
      "rob": ["You take all the money in the vault, and leave the bank. You then become the number one suspect of the robbery, leading you to skip town. You won? [REVERSE ROBBERY ENDING]", "Start over", "retry", "Quit", "quit"], 
      "return": ["You return to the bank lobby, The police arrive and rescue the hostages. You are hailed as a hero. You won. [HERO ENDING]", "Start over", "retry", "Quit", "quit"],
      }
    return game

def playNode(game, currentKey):
    currentNode = game[currentKey]
    (description, menu1, node1, menu2, node2) = currentNode
    print(f"""
{description}

1. {menu1}
2. {menu2}
    """)
    userChoice = input("What will you do?: ")
    
    if userChoice == "1":
        newKey = node1
    elif userChoice == "2":
        newKey = node2
    else:
        print("Please choose 1 or 2")
        newKey = currentKey
        
    return newKey

def main():
    game = makeGame()
    currentKey = "start"
    
    keepGoing = True
    while keepGoing:
        if currentKey == "quit":
            keepGoing = False
        else:
            currentKey = playNode(game, currentKey)

main()
