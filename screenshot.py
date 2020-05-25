import mss
import mss.tools

for i in range (1,100):
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": 300, "left": 40, "width": 605, "height": 208}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

    
        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)
