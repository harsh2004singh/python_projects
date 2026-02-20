import pywhatkit as kit

txt =""" Give me wisdom and courage.
A righteous and faithful leader I'll be,
So I may live through you, Lord,
An example of good I may be.

Teach me patience and understanding,
Grant me compassion and kindness too,
So my daughters may desire a tender heart,
Being kind, forgiving, and true.

Help me show them the way to salvation,
Lord, and the value of their souls,
So they may sustain love, hope, and faith,
That will lead them on their pathway home.

Remind me to hold them tightly
And tenderly let them go
So they might feel my comfort and love
When at times they may feel alone.

And in our body's absence, Lord,
I'm praying they may know
The only need that they would have
Is what I've instilled in their heart and soul."""

try:
    kit.text_to_handwriting(txt, "mother_poem.png", [0, 0, 138])
    print("Handwriting image created successfully!")
except Exception as e:
    print("Error occurred:", e)