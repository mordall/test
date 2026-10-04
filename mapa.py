# pip install gpxpy folium
import glob, os, gpxpy, folium
from collections import defaultdict

files = glob.glob("*.gpx")
m = folium.Map(tiles="OpenStreetMap", control_scale=True, prefer_canvas=True)

colors = ["red", "blue", "green", "purple", "orange", "darkred",
          "cadetblue", "black", "pink", "darkgreen"]

# Najpierw zbierz wszystkie unikalne lata
years_seen = set()
file_years = {}
for f in sorted(files):
    with open(f, encoding="utf-8") as fh:
        gpx = gpxpy.parse(fh)
    start = gpx.get_time_bounds().start_time
    year = start.year if start else "brak daty"
    file_years[f] = year
    years_seen.add(year)

# Przypisz każdemu rokowi kolor na stałe, z góry
sorted_years = sorted(years_seen, key=lambda y: (y == "brak daty", y))
color_map = {year: colors[i % len(colors)] for i, year in enumerate(sorted_years)}

groups = {}
all_pts = []

for f in sorted(files):
    year = file_years[f]
    if year not in groups:
        groups[year] = folium.FeatureGroup(name=str(year)).add_to(m)
    color = color_map[year]

    with open(f, encoding="utf-8") as fh:
        gpx = gpxpy.parse(fh)
    km = gpx.length_3d() / 1000
    for trk in gpx.tracks:
        for seg in trk.segments:
            pts = [(p.latitude, p.longitude) for p in seg.points]
            if len(pts) < 2:
                continue

            pl = folium.PolyLine(
                pts, weight=3, opacity=0.7, color=color,
                tooltip=f"{os.path.basename(f)} ({km:.1f} km)",
            ).add_to(groups[year])

            m.get_root().script.add_child(folium.Element(f"""
                window.addEventListener('load', function() {{
                    {pl.get_name()}.on('mouseover', function(e) {{
                        e.target.setStyle({{weight: 7, opacity: 1}});
                        e.target.bringToFront();
                    }});
                    {pl.get_name()}.on('mouseout', function(e) {{
                        e.target.setStyle({{weight: 3, opacity: 0.7}});
                    }});
                }});
            """))

            all_pts += pts

m.fit_bounds([[min(p[0] for p in all_pts), min(p[1] for p in all_pts)],
              [max(p[0] for p in all_pts), max(p[1] for p in all_pts)]])
folium.LayerControl(collapsed=False).add_to(m)
m.save("moje_trasy.html")