/*
You get any card as an argument. Your task is to return the suit of this card (in lowercase).

Our deck (is preloaded):

deck = ['2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣','A♣',
        '2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦','A♦',
        '2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♥',
        '2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠','A♠'];
*/

extern const char *const deck[52];

enum CardSuit { CLUBS, DIAMONDS, HEARTS, SPADES };

enum CardSuit get_suit (const char *card)
{
	int i;  
  for(i=0; i<52; i++)
    {
        if(deck[i] == card)
            break;
    }
  if(i < 13){return CLUBS;}
  else{
    if(i < 26){return DIAMONDS;}
    else{
      if(i < 39){return HEARTS;}
      else{
        return SPADES;
      }
    }
  }
}
