"""
File: my_drawing.py
Name:  Zoe Lai
----------------------
Displays image of an owl standing on a rod at night.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Owl and the moonlit sky
    -------------------------------------------------------------------------
    This owl, a friend of Duo from Duolingo, hates learning new languages but
    enjoys gazing at the night sky during full moons.
    """
    window = GWindow(width=800, height=600, title='owl')

    # background
    bg = GRect(width=window.width, height=window.height)
    bg.filled = True
    bg.fill_color = 'midnightblue'
    bg.color = 'midnightblue'

    # moon
    moon = GOval(width=120, height=120)
    moon.filled = True
    moon.fill_color = 'lightyellow'
    moon.color = 'lightyellow'

    # rod
    rod = GRect(width=window.width, height=30)
    rod.filled = True
    rod.fill_color = 'gray'
    rod.color = 'gray'

    # head
    head = GOval(width=200, height=180)
    head.filled = True
    head.fill_color = 'rosybrown'
    head.color = 'rosybrown'

    # wings
    wings = GOval(width=310, height=250)
    wings.filled = True
    wings.fill_color = 'brown'
    wings.color = 'brown'

    # body
    body = GOval(width=250, height=270)
    body.filled = True
    body.fill_color = 'rosybrown'
    body.color = 'rosybrown'

    # eyesockets
    l_eye_socket = GOval(width = 100, height = 100)
    l_eye_socket.filled = True
    l_eye_socket.fill_color = 'peachpuff'
    l_eye_socket.color = 'peachpuff'
    r_eye_socket = GOval(width = 100, height = 100)
    r_eye_socket.filled = True
    r_eye_socket.fill_color = 'peachpuff'
    r_eye_socket.color = 'peachpuff'

    # eyeballs
    l_eyeball = GOval(width = 45, height = 45)
    l_eyeball.filled = True
    l_eyeball.fill_color = 'sienna'
    l_eyeball.color = 'sienna'
    r_eyeball = GOval(width = 45, height = 45)
    r_eyeball.filled = True
    r_eyeball.fill_color = 'sienna'
    r_eyeball.color = 'sienna'

    # beak
    beak = GPolygon()
    beak.add_vertex((390, 200))
    beak.add_vertex((413, 200))
    beak.add_vertex((402, 240))
    beak.filled = True
    beak.fill_color = 'firebrick'
    beak.color = 'firebrick'

    # l_ear
    l_ear = GPolygon()
    l_ear.add_vertex((300, 90))
    l_ear.add_vertex((300, 170))
    l_ear.add_vertex((340, 100))
    l_ear.filled = True
    l_ear.fill_color = 'rosybrown'
    l_ear.color = 'rosybrown'

    # r_ear
    r_ear = GPolygon()
    r_ear.add_vertex((500, 90))
    r_ear.add_vertex((500, 170))
    r_ear.add_vertex((460, 100))
    r_ear.filled = True
    r_ear.fill_color = 'rosybrown'
    r_ear.color = 'rosybrown'

    # paws
    l_paw1 = GOval(width = 15, height = 30)
    l_paw1.filled = True
    l_paw1.fill_color = 'orange'
    l_paw1.color = 'orange'

    l_paw2 = GOval(width = 14, height = 35)
    l_paw2.filled = True
    l_paw2.fill_color = 'orange'
    l_paw2.color = 'orange'

    l_paw3 = GOval(width = 15, height = 30)
    l_paw3.filled = True
    l_paw3.fill_color = 'orange'
    l_paw3.color = 'orange'

    r_paw1 = GOval(width = 15, height = 30)
    r_paw1.filled = True
    r_paw1.fill_color = 'orange'
    r_paw1.color = 'orange'

    r_paw2 = GOval(width = 14, height = 35)
    r_paw2.filled = True
    r_paw2.fill_color = 'orange'
    r_paw2.color = 'orange'

    r_paw3 = GOval(width = 15, height = 30)
    r_paw3.filled = True
    r_paw3.fill_color = 'orange'
    r_paw3.color = 'orange'

    # objects added to window
    window.add(bg)
    window.add(rod, 0, 485)
    window.add(moon, 40, 32)
    window.add(head, x= (window.width-head.width)/2, y = 80)
    window.add(wings, x=(window.width - wings.width) / 2, y= head.y + head.height - 15)
    window.add(body, x= (window.width-body.width)/2, y = head.y + head.height - 25)
    window.add(l_eye_socket, x=((window.width - l_eye_socket.width) / 2) - 40, y=head.y + 40)
    window.add(r_eye_socket, x=((window.width - r_eye_socket.width) / 2) + 40, y=head.y + 40)
    window.add(l_eyeball, x= l_eye_socket.x+l_eye_socket.width/3, y=l_eye_socket.y+l_eye_socket.height/2 - 10)
    window.add(r_eyeball, x=r_eye_socket.x + r_eye_socket.width / 4, y=r_eye_socket.y + r_eye_socket.height / 2 - 10)
    window.add(beak)
    window.add(l_ear)
    window.add(r_ear)
    window.add(l_paw1, 330, 480)
    window.add(l_paw2, 340, 480)
    window.add(l_paw3, 350, 480)
    window.add(r_paw1, 440, 480)
    window.add(r_paw2, 450, 480)
    window.add(r_paw3, 460, 480)


if __name__ == '__main__':
    main()
