import os
import cv2

list_of_names = []


def delete_old_data():
   for i in os.listdir("generated-certificates/"):
      os.remove("generated-certificates/{}".format(i))


def cleanup_data():
   with open('name-data.txt') as f:
      for line in f:
          list_of_names.append(line.strip())


def generate_certificates():

   for index, name in enumerate(list_of_names):
      certificate_template_image = cv2.imread("certificate-template.jpg")
      cv2.putText(certificate_template_image, name.strip(), (815,1500), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 250), 5, cv2.LINE_AA)
      cv2.imwrite("generated-certificates/{}.jpg".format(name.strip()), certificate_template_image)
      print("Processing {} / {}".format(index + 1,len(list_of_names)))
      


def main():
   delete_old_data()
   cleanup_data()
   generate_certificates()



if __name__ == '__main__':
   main()

