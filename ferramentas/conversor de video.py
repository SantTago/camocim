from moviepy.editor import VideoFileClip

def converter_mkv_para_mp4(input_file, output_file):
    # Carregar o vídeo
    video_clip = VideoFileClip(input_file)

    # Salvar o vídeo no formato MP4
    video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    # Substitua 'input_video.mkv' pelo caminho do seu vídeo MKV de entrada
    input_video = 'C:\\Users\\mocob\\Videos\\Nova pasta'
    
    # Substitua 'output_video.mp4' pelo nome desejado para o vídeo de saída
    output_video = 'C:\\Users\\mocob\\Videos\\Nova pasta'

    converter_mkv_para_mp4(input_video, output_video)



