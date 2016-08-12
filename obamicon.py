# skeleton code for obamicon
from PIL import Image
panda=Image.open("panda.jpg")
# panda.getdata()
# panda.show()

# ===============================================================
# define colors as variables so we can recall them later:
# dark blue: (0, 51, 76)
# red: (217, 26, 33)
# light blue: (112, 150, 158)
# yellow: (252, 227, 166)
# ===============================================================
dark_blue= (0,51,76)
red= (217,26,33)
light_blue= (112,150,158)
yellow= (252,227,166)
# ===============================================================
# define a function that obama-fies the image.
# this function will take your images' pixel list as a parameter.
# for each pixel in your image's pixel list, "obama-fy" it by 
# creating a new RGB value (dark blue, red, light blue, or yellow) 
# based on the intensity of that pixel. return a pixel list 
# containing the RGB values of the obamafied picture.
# ===============================================================
panda=Image.open("panda.jpg")
panda.getdata() 
new_list=[]
pixellist= list(panda.getdata())
def obamafy(pixel_list):
	# panda.getdata() 
	for item in pixel_list:
		intensity= item[0] + item[1] + item [2]
		if intensity <182:
			new_list.append(dark_blue)
		elif intensity >=182 and intensity<364:
			new_list.append(red)
		elif intensity >=364 and intensity<546:
			new_list.append(light_blue)
		else:
			new_list.append(yellow)
	return new_list
panda2=obamafy(pixellist) 
# panda.show()



# ===============================================================
# ask the user for the image name and open the image
# ===============================================================


# ===============================================================
# convert the image into a list of pixel RGB values
# ===============================================================

# ===============================================================
# obamafy your image by calling your function
# ===============================================================

# ===============================================================
# create a new image and copy the new obama-fied pixel list into the image
# ===============================================================
newpanda= Image.new("RGB", panda.size)
newpanda.putdata(panda2)
newpanda.save("newpanda.jpg")
newpanda.show() 
# ===============================================================
# finally, show and save the image
# ===============================================================

