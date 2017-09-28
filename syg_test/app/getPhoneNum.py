import os


@staticmethod
class GetPhoneNum():

    @staticmethod
    def get_photo_num():
        # print(os.getcwd())
        phone_num = 13800002000
        with open('./syg_test/app/phonenum.txt', 'r') as phone_file:
            line = phone_file.readline()
            if len(line) > 0:
                print(int(line[-1]))
                phone_num_old = line[-1]
                phone_num = int(phone_num_old) + 1

        with open('./syg_test/app/phonenum.txt', 'w') as phone_file:
            phone_file.write(str(phone_num) + '\n')

            print(str(phone_num))

        return phone_num






