from sys import orig_argv
import librosa
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
        wav_filename= wav.replace(data_folder,save_folder)
        song_16K,sr=librosa.load(wav,16000)
        song_8K=librosa.resample(y=song_16K,orig_sr=16000,targe=8000)
        librosa.output.write_wav(wav_filename,song_8K,8000)
        



main()


