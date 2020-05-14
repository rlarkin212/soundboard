import simpleaudio as sa
import sys


def playSound(num):
    files = ['bruh2',
             'nonce',
             'massiveLegend',
             'edp445',
             'bruh4']

    if num < len(files):
        wave_obj = sa.WaveObject.from_wave_file(f'sounds/{files[num]}.wav')
        play_obj = wave_obj.play()
        play_obj.wait_done()
    else:
        print(f'out of index {len(files)} sounds')


if __name__ == "__main__":
    playSound(int(sys.argv[1]))
