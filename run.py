import cv2

list_of_names = []


def clean_data():

   with open('name-data.txt') as f:
      for line in f:
          list_of_names.append(line.strip())


def delete_old_data():
   for i in os.listdir("generated-certificates/"):
      os.remove(i)

def generate_certificates():

   for name in list_of_names:
      certificate_template_image = cv2.imread("certificate-template.jpg")
      cv2.putText(certificate_template_image, line.strip(), (815,1500), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 250), 5, cv2.LINE_AA)
      cv2.imwrite("generated-certificates/{}.jpg".format(line.strip()), certificate_template_image)
      print(line.strip())

