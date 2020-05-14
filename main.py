import simpleaudio as sa

def play(num):
    files = ['bruh2.wav', 'nonce.wav', 'massiveLegend.wav']
    if num < len(files):
        wave_obj = sa.WaveObject.from_wave_file(f'sounds/{files[num]}')
        play_obj = wave_obj.play()
        play_obj.wait_done()
    else:
        print(f'out of index {len(files)} sounds')

play(2)
