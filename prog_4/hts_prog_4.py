import os, subprocess
import pygame

import xml
import xml.etree.ElementTree as ET


DEBUG = True
red = (255, 0, 0)

class PlotMe:

	def __init__(self):
		self.tree = None
		self.root = None

		self.elements = []
		self.surface = pygame.display.set_mode((1000,1000)) 
		#self.surface.fill('white')
		#pygame.display.update()

	def load_xml(self):
		if not DEBUG:
			subprocess.call(['bzip2', '-d', '/cygdrive/j/tj/downloads/plotMe.xml.bz2'])
			self.tree = ET.parse('/cygdrive/j/tj/downloads/plotMe.xml')
		else:
			self.tree = ET.parse('plotMe.xml')
		self.root = self.tree.getroot()

	def parse_xml(self):
		for ele in self.root:
			draw_params = {'Type': ele.tag}
			for attrib in ele:
				if attrib.tag == 'Color':
					draw_params[attrib.tag] = attrib.text
				else:
					draw_params[attrib.tag] = float(attrib.text)
			#if DEBUG: print draw_params
			self.elements.append(draw_params)

	def draw_elements(self):
		for e in self.elements:
			if e['Type'] == 'Line':
				start = (e['XStart'], e['YStart'])
				end = (e['XEnd'], e['YEnd'])
				pygame.draw.line(self.surface, red, start, end)	
				pygame.display.update()

			elif e['Type'] == 'Arc':
				r = e['Radius']
				rectangle = pygame.Rect((e['XCenter'] - r), (e['YCenter'] + r), 2*r, 2*r)
				print str(rectangle.height)
				pygame.draw.arc(self.surface, rectangle, red, e['ArcStart'], e['ArcExtend'])
				pygame.display.update()

	def drawHouse(x, y, width, height, screen, color):
	    points = [(x,y- ((2/3.0) * height)), (x,y), (x+width,y), (x+width,y-(2/3.0) * height), 
	        (x,y- ((2/3.0) * height)), (x + width/2.0,y-height), (x+width,y-(2/3.0)*height)]
	    lineThickness = 2
	    pygame.draw.lines(screen, color, False, points, lineThickness)

def main():
	pygame.init()
	pm = PlotMe()
	pm.load_xml()
	pm.parse_xml()
	pm.draw_elements()
	#pygame.Surface.blit(pm.surface)
#	pygame.display.update()
	return pm

def delete():
	del(pm)

if __name__ == '__main__':
	main()

