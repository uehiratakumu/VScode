import pandas as pd
 
url = 'https://www.booking.com/hotel/jp/pagong-with-m-39-s-jing-du-shi.ja.html?label=gen173nr-1FCAEoggI46AdIM1gEaHWIAQGYARW4AQfIAQzYAQHoAQH4AQuIAgGoAgO4AtjW54kGwAIB0gIkYjBjMTgzMDYtYmI3Zi00ZTI2LWI4OTYtYzdlODk2NjUwNTQ52AIG4AIB;sid=2503187a7950468c4a73ac3688c8eaad;all_sr_blocks=697939301_287955722_2_0_0;checkin=2021-10-14;checkout=2021-10-15;dest_id=-235402;dest_type=city;dist=0;group_adults=1;group_children=0;hapos=1;highlighted_blocks=697939301_287955722_2_0_0;hpos=1;no_rooms=1;req_adults=1;req_children=0;room1=A;sb_price_type=total;sr_order=popularity;sr_pri_blocks=697939301_287955722_2_0_0__299999;srepoch=1631192320;srpvid=5fe45b3f21160288;type=total;ucfs=1&#hotelTmpl'
df = pd.read_html(url)
print(df[1])
