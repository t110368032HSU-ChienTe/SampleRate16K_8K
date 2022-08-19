from pydub import AudioSegment
import glob
import os
data_folder ='clean'
save_folder ='clean_8K'
sample_rate=8000

wavs_list= glob.glob(f'{data_folder}/*.wav')

def main(wavs_list=wavs_list):
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    for wav in wavs_list:
        print(f'處理{wav}')
        wav_filename=f'{save_folder}/{wav}'
        song=AudioSegment.from_wav(f'{data_folder}/{wav}')
        song.set_frame_rate(sample_rate).export(wav_filename,format="wav")


main()


