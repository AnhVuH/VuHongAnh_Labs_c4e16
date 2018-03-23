from youtube_dl import YoutubeDL

dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=6OVt1RG2V9w'])

dl.download(['https://www.youtube.com/watch?v=1u0ygl9vJHI','https://www.youtube.com/watch?v=XszJkmsrccI&t=104s'])

options = {
        'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=-MfGnmeWrBw'])

options = {
    'default_search': 'ytsearch',
    'max_downloads' : 1
}
dl=YoutubeDL(options)
dl.download(['Những mùa xuân bỏ lại Lộn Xộn'])


options = {
        'default_search':'ytsearch',
        'max_download': 1,
        'format':'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['1080 phạm toàn thắng'])
