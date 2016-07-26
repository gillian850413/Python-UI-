# -*- coding: utf-8 -*-
#!/usr/bin/python3
import gi, sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf, Pango
import time, cairo



class MyWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="User Information")
		self.set_name('MyWindow')
		self.set_default_size(560, 315)


		overlay = Gtk.Overlay.new()
	
		#Gtk Overlay
		#drawing area
		area = Gtk.DrawingArea()
		area.set_size_request(560, 315)
		area.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse('#aeebff'))

		area.connect('draw', self.draw_bg)
		area.connect('draw', self.area_upper)
		area.connect('draw', self.area_lower)
		area.connect('draw', self.logo)
		overlay.add(area)


		#label/left window
		label1 = Gtk.Label('name')
		label1.set_alignment(62/560.0, 112/315.0)
		label1.modify_fg(Gtk.StateType.NORMAL, Gdk.color_parse('#000000'))
		label1.modify_font(Pango.FontDescription("Granada 11"))
		overlay.add_overlay(label1)
		

		label2 = Gtk.Label('info')
		label2.set_alignment(62/560.0, 192/315.0)
		label2.modify_fg(Gtk.StateType.NORMAL, Gdk.color_parse('#000000'))
		label2.modify_font(Pango.FontDescription("Granada 11"))
		overlay.add_overlay(label2)

		#label/right window
		now = time.strftime('%Y/%m/%d %H:%M:%S')
		items = ['sid', 'cid', now, 'location', 'contact']
		y = 75
		for i in range(5):
			locals()["group"+str(i+3)] = Gtk.Label(items[i])
			locals()["group"+str(i+3)].set_alignment(500/560.0, y/315.0)
			locals()["group"+str(i+3)].modify_fg(Gtk.StateType.NORMAL, Gdk.color_parse('#000000'))
			locals()["group"+str(i+3)].modify_font(Pango.FontDescription("Granada 11"))
			y += 43
			overlay.add_overlay(locals()["group"+str(i+3)])
		self.add(overlay)
		self.show_all()
	
	#system background
	def draw_bg(self, area, cr):
		#background rectangles
		cr.set_source_rgb(0.7686, 0.9529, 1.0)
		cr.rectangle(20, 20, 520, 275) #x0 y0 x1 y1
		cr.fill()		
		
		cr.set_source_rgb(0.9059, 0.9804, 1.0)
		cr.rectangle(25, 15, 510, 285)
		cr.fill()	

		cr.set_source_rgb(1.0, 1.0, 1.0)
		cr.rectangle(33, 10, 494, 295)
		cr.fill()
		
		#line
		#set_line_width
		cr.set_source_rgb(0.8824, 0.8902, 0.8941)	
		cr.set_line_width(1)
		cr.move_to (335, 60) # Line to (x,y)
		cr.line_to (335, 305) # Line to (x,y)
		
		cr.move_to (35, 60) # Line to (x,y)
		cr.line_to (525, 60) # Line to (x,y)
		cr.stroke()
		return

	def area_upper(self, area, cr):
		cr.set_source_rgb(0.0745, 0.2588, 0.4784)
		#cr.select_font_face('KacstDigital', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)	
		cr.set_font_size(30)
		cr.move_to(205, 50)		
		cr.show_text("樂   學   網")
		return	
	
	def area_lower(self, area, cr):
		#lower left window(name, other info)
		cr.set_source_rgb(0.0745, 0.0745, 0.0745)
		#cr.select_font_face('KacstDigital', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)	
		cr.set_font_size(16)
		cr.move_to(88, 90)		
		cr.show_text("姓名: ")

		cr.move_to(88, 165)		
		cr.show_text("課程資訊: ")		

		#area for name input
		cr.set_source_rgba(0.8824, 0.8902, 0.8941)
		cr.rectangle(50, 102, 200, 28)
		cr.fill()	
		
		#area for other info input
		cr.set_source_rgba(0.8824, 0.8902, 0.8941)
		cr.rectangle(50, 176, 270, 110)
		cr.fill()

		#lower right window
		yarea = 61
		for i in range(5):
			if i%2 == 0:
				cr.set_source_rgba(0.8824, 0.8902, 0.8941)				
			else:
				cr.set_source_rgba(1.0, 1.0, 1.0)

			cr.rectangle(336, yarea, 190, 40)
			cr.fill()			
			yarea += 40		
		return	

	def logo(self, area, cr):	
		#keelung education center logo
		img = GdkPixbuf.Pixbuf.new_from_file_at_size("icon/edu.jpg", 130, 140)
		Gdk.cairo_set_source_pixbuf(cr, img, 340, 270)		
		cr.paint()
		
		#NCHC logo
		img = GdkPixbuf.Pixbuf.new_from_file_at_size("icon/nchc.jpg", 55, 50)
		Gdk.cairo_set_source_pixbuf(cr, img, 470, 262)		
		cr.paint()

		#sid, cid, time, location, contact icon
		icons = ['icon/sid.png', 'icon/cid.png', 'icon/time.png', 'icon/location.png', 'icon/contact.png', 'icon/name.png', 'icon/note.png']
		
		yLeft = 65 #left window
		yRight = 65 #right window
		for i in range(len(icons)):
			img = GdkPixbuf.Pixbuf.new_from_file_at_size(icons[i], 31, 31)
			if i < 5: 
				Gdk.cairo_set_source_pixbuf(cr, img, 340, yRight)		
				cr.paint()
				yRight += 40
			else:
				Gdk.cairo_set_source_pixbuf(cr, img, 50, yLeft)		
				cr.paint()				
				yLeft += 75
		return

	
def main(argv):

    win = MyWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main(sys.argv)
