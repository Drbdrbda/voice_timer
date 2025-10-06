from vosk import Model, KaldiRecognizer
import pyaudio
import json

model = Model("vosk-model-small-ru-0.22")
rec = KaldiRecognizer(model, 16000)
pa = pyaudio.PyAudio()

number_dict = {
    'ноль': 0,
    'нуль': 0,
    'один': 1, 
    'два': 2, 
    'три': 3, 
    'четыре': 4, 
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9,
    'десять': 10,
    'одинадцать': 11,
    'двенадцать': 12,
    'тринадцать': 13,
    'четырнадцать': 14,
    'пятнадцать': 15,
    'шестнадцать': 16,
    'семнадцать': 17,
    'восемнадцать': 18,
    'девятнадцать': 19,
    'двадцать': 20,
    'тридцать': 30,
    'сорок': 40,
    'пятьдесят': 50,
    'шестьдесят': 60,
    'семьдесят': 70,
    'восемьдесят': 80,
    'девяносто': 90,
    'сто': 100,
    'двести': 200,
    'триста': 300,
    'четыреста': 400,
    'пятьсот': 500,
    'шестьсот': 600,
    'семьсот': 700,
    'восемьсот': 800,
    'девятьсот': 900,
    'тысяча': 1000
}

units_of_time_dict = {
    'секунд', 'секунды', 
    'минут', 'минуты',
    'час', 'часа', 'часы', 'часов'
}

stream = pa.open(
    format=pyaudio.paInt16, 
    channels=1, 
    rate=16000, 
    input=True, 
    frames_per_buffer=16000
)
stream.start_stream()

while True:
    data = stream.read(4000)

    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        text = result.get('text', '')

        if text:
            print(f'Распознано: {text}')

            numbers = []
            user_units_of_time = ''
            #new_numbers = []

            words = text.split()
            for word in words:
                if word in number_dict:
                    numbers.append(number_dict[word])
                if word in units_of_time_dict:
                    user_units_of_time += word


            if len(numbers) > 0:
                new_numbers = sum(numbers)

                print(f'Распознанные числа: {numbers}')
                print(f'хорошо, таймер поставлен на {new_numbers} {user_units_of_time}')

            if 'стоп' in text.lower():
                break


                # for i in range(len(numbers) - 1, -1, -1):
                #     if numbers[i] < numbers[i-1]:
                #         new_numbers.append(sum(numbers))
                #         break
                #     if numbers[i] < 10:
                #         new_numbers.append(numbers[i])
                    # if numbers[i] >= 20 and numbers[i+1] < 10:
                    #     new_number = numbers[i] + numbers[i+1]
                    #     new_numbers.append(new_number)
                    #     if numbers[i] >= 100 and new_number < 100:
                    #         new_number = numbers[i] + new_number
                    #         new_numbers.append(new_number)

