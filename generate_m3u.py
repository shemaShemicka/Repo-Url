import os

def create_m3u():
    input_file = 'MacDataBase.txt'
    output_file = 'playlist.m3u'
    
    if not os.path.exists(input_file):
        return

    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        f.write('#EXTM3U\n')
        for line in lines:
            line = line.strip()
            if '|' in line:
                portal, mac = line.split('|')
                # Sreduvanje na URL-to
                base_url = portal.strip()
                m3u_link = f"{base_url}?mac={mac.strip()}"
                
                # Ime na kanalot spored portalot
                name = base_url.split("//")[-1].split("/")[0]
                f.write(f'#EXTINF:-1, Portal: {name}\n')
                f.write(f'{m3u_link}\n')

if __name__ == "__main__":
    create_m3u()
