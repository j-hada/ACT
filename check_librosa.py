import librosa
import soundfile as sf

audio_file = 'C:\\Users\\jdi04\\Documents\\GitHub\\ACT\\240314 on my mind demo_BOUNCE.wav'

y, sr = librosa.load(audio_file, sr=None) 

print(f"샘플링 레이트: {sr}, 길이: {len(y)} 샘플")

output_file = 'output_audio.wav' 

sf.write(output_file, y, sr)
print(f"{output_file} 파일이 저장되었습니다.")
