# data will be in subset folder in the main folder
def download_data(subset, output_folder='main', subset_folder='branch'):
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    if not os.path.exists(os.path.join(output_folder, subset_folder)):
        os.mkdir(os.path.join(output_folder, subset_folder))
        
    path = []
    for video in subset:
        for i, frame in enumerate(get_frames(video)):
            output_path = os.path.join(output_folder, subset_folder, 'frame_' + str(i) + '.jpg')
            if not os.path.exists(output_path):
                output_path = cv2.imwrite(f'{output_folder}/{subset_folder}/frame_{i}.jpg', frame)
            path.append(output_path)
    return path
