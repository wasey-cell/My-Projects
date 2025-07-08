from kivymd.app import MDApp  
from kivy.lang import Builder  
from kivymd.uix.dialog import MDDialog  
from kivymd.uix.button import MDRaisedButton,MDFlatButton, MDRoundFlatButton, MDRectangleFlatButton,MDFillRoundFlatIconButton,MDRoundFlatIconButton,MDRectangleFlatIconButton  
from kivymd.uix.textfield import MDTextField  
from kivy.uix.boxlayout import BoxLayout  
from kivymd.uix.boxlayout import MDBoxLayout  
from kivymd.uix.label import MDLabel
from kivy.core.audio import SoundLoader 
from kivy.core.window import Window
from kivymd.uix.label import MDIcon
from kivy.graphics import Color, Line
from kivy.uix.widget import Widget
from kivy.clock import Clock  
import random  
  
kv = '''
<MDRaisedButton>:
    on_press: app.game(self)
    font_size: 70

Screen:
    FloatLayout:

        MDBoxLayout:
            orientation: 'vertical'
            size_hint: 1, 1

            MDLabel:
                text: 'X0X Gam€'
                halign: 'center'
                font_size: '50sp'
                size_hint_y: 0.1
                theme_text_color: 'Custom'
                text_color: app.theme_cls.primary_color

            MDGridLayout:
                cols: 2
                size_hint_y: 0.1
                spacing :10

                MDLabel:
                    id: play1
                    text: 'score'
                    halign: 'center'
                    font_style: 'H5'
                    theme_text_color: 'Custom'
                    text_color: app.theme_cls.primary_color

                MDLabel:
                    id: play2
                    text: 'score'
                    halign: 'center'
                    font_style: 'H5'
                    theme_text_color: 'Custom'
                    text_color: app.theme_cls.primary_color

            MDGridLayout:
                id: button_grid
                cols: 5
                spacing: 1
                size_hint_y: 0.8
                pos_hint: {'top': 1}

                MDRaisedButton:
                    id: p1
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p2
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p3
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p4
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p5
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p6
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p7
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p8
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p9
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p10
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p11
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p12
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p13
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p14
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p15
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p16
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p17
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p18
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p19
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p20
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p21
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p22
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p23
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p24
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p25
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p26
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p27
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p28
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p29
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p30
                    text: ''
                    size_hint: 1, 1

        # Overlay highlight layer exactly on buttons grid
        Widget:
            id: highlight_layer
            size_hint_y: 0.8
            size_hint_x: 1
            pos_hint: {'top': 0.9}
'''
  
class mdApp(MDApp):  
    def build(self):  
        self.theme_cls.theme_style = 'Light'  
        root = Builder.load_string(kv)
        self.highlight_layer = root.ids.highlight_layer
        self.dialog = None  
        self.pp1 = ''  
        self.pp2 = ''  
        self.p1s = 0  
        self.p2s = 0  
        self.end = 0
        self.colors = [  
            "Red", "Pink", "Purple", "DeepPurple", "Indigo", "Blue", "LightBlue",  
            "Cyan", "Teal", "Green", "LightGreen", "Lime", "Yellow", "Amber",  
            "Orange", "DeepOrange", "Brown", "Gray", "BlueGray"  
        ]  
        b = root.ids  
        self.win = [  
            (b.p1, b.p2, b.p3), (b.p2, b.p3, b.p4), (b.p3, b.p4, b.p5),  
            (b.p6, b.p7, b.p8), (b.p7, b.p8, b.p9), (b.p8, b.p9, b.p10),  
            (b.p11, b.p12, b.p13), (b.p12, b.p13, b.p14), (b.p13, b.p14, b.p15),  
            (b.p16, b.p17, b.p18), (b.p17, b.p18, b.p19), (b.p18, b.p19, b.p20),  
            (b.p21, b.p22, b.p23), (b.p22, b.p23, b.p24), (b.p23, b.p24, b.p25),  
            (b.p26, b.p27, b.p28), (b.p27, b.p28, b.p29), (b.p28, b.p29, b.p30),  
            (b.p1, b.p6, b.p11), (b.p6, b.p11, b.p16), (b.p11, b.p16, b.p21), (b.p16, b.p21, b.p26),  
            (b.p2, b.p7, b.p12), (b.p7, b.p12, b.p17), (b.p12, b.p17, b.p22), (b.p17, b.p22, b.p27),  
            (b.p3, b.p8, b.p13), (b.p8, b.p13, b.p18), (b.p13, b.p18, b.p23), (b.p18, b.p23, b.p28),  
            (b.p4, b.p9, b.p14), (b.p9, b.p14, b.p19), (b.p14, b.p19, b.p24), (b.p19, b.p24, b.p29),  
            (b.p5, b.p10, b.p15), (b.p10, b.p15, b.p20), (b.p15, b.p20, b.p25), (b.p20, b.p25, b.p30),  
            (b.p1, b.p7, b.p13), (b.p2, b.p8, b.p14), (b.p3, b.p9, b.p15),  
            (b.p6, b.p12, b.p18), (b.p7, b.p13, b.p19), (b.p8, b.p14, b.p20),  
            (b.p11, b.p17, b.p23), (b.p12, b.p18, b.p24), (b.p13, b.p19, b.p25),  
            (b.p16, b.p22, b.p28), (b.p17, b.p23, b.p29), (b.p18, b.p24, b.p30),  
            (b.p3, b.p7, b.p11), (b.p4, b.p8, b.p12), (b.p5, b.p9, b.p13),  
            (b.p8, b.p12, b.p16), (b.p9, b.p13, b.p17), (b.p10, b.p14, b.p18),  
            (b.p13, b.p17, b.p21), (b.p14, b.p18, b.p22), (b.p15, b.p19, b.p23),  
            (b.p18, b.p22, b.p26), (b.p19, b.p23, b.p27), (b.p20, b.p24, b.p28),  
        ]  
        self.theme_cls.primary_palette = random.choice(self.colors)  
        self.dialog_open = False  
        self.gameend=False
        self.repeat = []  
        self.turn = 'p1'  
        return root
    def reset(self):
        self.game_over_dialog.dismiss()
        self.highlight_layer.canvas.clear()
        sound=SoundLoader.load('sharp-pop-328170.mp3')
        sound.play()
        b=self.root.ids
        for i in range(1,31):
        	b[f'p{i}'].text=''
        self.dialog = None
        self.pp1 = ''
        self.pp2 = ''
        self.p1s = 0
        self.p2s = 0
        self.end = 0
        self.theme_cls.primary_palette = random.choice(self.colors)
        self.root.do_layout()
        self.dialog_open = False
        self.gameend=False
        self.repeat = []
        self.turn = 'p1'
        self.on_start()
        self.root.ids.play1.text = f'{self.pp1} score\n{self.p1s}'
        self.root.ids.play2.text = f'{self.pp2} score\n{self.p2s}'
        self.win = [  
            (b.p1, b.p2, b.p3), (b.p2, b.p3, b.p4), (b.p3, b.p4, b.p5),  
            (b.p6, b.p7, b.p8), (b.p7, b.p8, b.p9), (b.p8, b.p9, b.p10),  
            (b.p11, b.p12, b.p13), (b.p12, b.p13, b.p14), (b.p13, b.p14, b.p15),  
            (b.p16, b.p17, b.p18), (b.p17, b.p18, b.p19), (b.p18, b.p19, b.p20),  
            (b.p21, b.p22, b.p23), (b.p22, b.p23, b.p24), (b.p23, b.p24, b.p25),  
            (b.p26, b.p27, b.p28), (b.p27, b.p28, b.p29), (b.p28, b.p29, b.p30),  
            (b.p1, b.p6, b.p11), (b.p6, b.p11, b.p16), (b.p11, b.p16, b.p21), (b.p16, b.p21, b.p26),  
            (b.p2, b.p7, b.p12), (b.p7, b.p12, b.p17), (b.p12, b.p17, b.p22), (b.p17, b.p22, b.p27),  
            (b.p3, b.p8, b.p13), (b.p8, b.p13, b.p18), (b.p13, b.p18, b.p23), (b.p18, b.p23, b.p28),  
            (b.p4, b.p9, b.p14), (b.p9, b.p14, b.p19), (b.p14, b.p19, b.p24), (b.p19, b.p24, b.p29),  
            (b.p5, b.p10, b.p15), (b.p10, b.p15, b.p20), (b.p15, b.p20, b.p25), (b.p20, b.p25, b.p30),  
            (b.p1, b.p7, b.p13), (b.p2, b.p8, b.p14), (b.p3, b.p9, b.p15),  
            (b.p6, b.p12, b.p18), (b.p7, b.p13, b.p19), (b.p8, b.p14, b.p20),  
            (b.p11, b.p17, b.p23), (b.p12, b.p18, b.p24), (b.p13, b.p19, b.p25),  
            (b.p16, b.p22, b.p28), (b.p17, b.p23, b.p29), (b.p18, b.p24, b.p30),  
            (b.p3, b.p7, b.p11), (b.p4, b.p8, b.p12), (b.p5, b.p9, b.p13),  
            (b.p8, b.p12, b.p16), (b.p9, b.p13, b.p17), (b.p10, b.p14, b.p18),  
            (b.p13, b.p17, b.p21), (b.p14, b.p18, b.p22), (b.p15, b.p19, b.p23),  
            (b.p18, b.p22, b.p26), (b.p19, b.p23, b.p27), (b.p20, b.p24, b.p28),  
        ]   	 
    def on_start(self):    
        if not self.dialog:  
            content = BoxLayout(orientation='vertical', spacing=20, padding=10, size_hint_y=None)  
            content.bind(minimum_height=content.setter('height'))  
  
            self.player1_input = MDTextField(  
                hint_text="Player 1 Name", icon_right='account', 
                size_hint_x=1,  
                pos_hint={"center_x": 0.5}  
            )  
            self.player2_input = MDTextField(  
                hint_text="Player 2 Name",icon_right='account' , 
                size_hint_x=1,  
                pos_hint={"center_x": 0.5}  
            )  
  
            content.add_widget(self.player1_input)  
            content.add_widget(self.player2_input)  
  
            self.dialog = MDDialog(  
                title="Enter Player Names\n",padding=10, 
                type="custom",  
                content_cls=content,  
                auto_dismiss=False,  
                buttons=[  
                    MDRectangleFlatIconButton(  
                        text="Let's Start",icon='play',  
                        on_press=self.sett  
                    )  
                ]  
            )  
        self.dialog.open()  
        self.dialog_open = True  
  
    def sett(self, dt=None):
        sound=SoundLoader.load('sharp-pop-328170.mp3')
        sound.play()  
        if self.player1_input.text and self.player2_input.text:  
            self.dialog.dismiss()  
            self.dialog_open = False  
            self.pp1 = self.player1_input.text  
            self.pp2 = self.player2_input.text
            if self.pp1==self.pp2:
            	self.pp2+='°'
            self.root.ids.play1.text = f'{self.pp1} [O] score\n{self.p1s}'
            self.root.ids.play2.text = f'{self.pp2} [X] score\n{self.p2s}'  	 
            self.toss()	 
  
    def stop(self):
        sound=SoundLoader.load('sharp-pop-328170.mp3')
        sound.play()   
        Window.close()
    def highlight_line(self, btns):
    	#self.highlight_layer.canvas.clear()
    	with self.highlight_layer.canvas:
    	   if self.turn=='p1':
    	   	Color(1,0,0,0.7)
    	   else:
    	   	Color(0,1,0,0.7)	
    	   coords = []
    	   for btn in btns:
    	   	coords.extend([btn.center_x, btn.center_y])
    	   if len(coords)>=4:
    	   	Line(points=coords, width=4)
    	   	
    def toss(self):
    	btn_heads = MDFillRoundFlatIconButton(text='Heads', icon='brain',on_press=lambda inst: self.toss_win('head'))
    	btn_tails = MDFillRoundFlatIconButton(text='Tails', icon='paw',on_press=lambda inst: self.toss_win('tail'))
    	self.toss_dialog = MDDialog(title='Toss',auto_dismiss=False,text=f'{self.pp1}’s call',buttons=[btn_heads, btn_tails])
    	self.toss_dialog.open()
    def toss_win(self,choice):
    	sound=SoundLoader.load('wood-surface-single-coin-payout-4-215284.mp3')
    	sound.play()
    	opt=['head','tail']
    	select=random.choice(opt)
    	if choice==select:
    		self.toss_dialog.text=f'{self.pp1} win the toss\nIts {self.pp1} turn first'
    		Clock.schedule_once(self.toss_dialog_dis,3)
    	else:
    		self.toss_dialog.text=f'{self.pp1} lost the toss\nIts {self.pp2} turn first'
    		self.turn='p2'
    		Clock.schedule_once(self.toss_dialog_dis,3)
    def toss_dialog_dis(self,dt=None):
    	self.toss_dialog.dismiss()			 
    def game(self, instance):
        sound=SoundLoader.load('sharp-pop-328170.mp3')
        sound.play()
        self.root.ids.play1.text = f'{self.pp1} [O] score\n{self.p1s}'  
        self.root.ids.play2.text = f'{self.pp2} [X] score\n{self.p2s}'  
  
        if self.dialog_open or self.gameend:  
            return  
  
        if instance not in self.repeat:  
            self.end += 1  
            if self.turn == 'p1':  
                instance.text = 'O'  
                self.repeat.append(instance)  
                self.check()  
                self.turn = 'p2'  
            else:  
                instance.text = 'X'  
                self.repeat.append(instance)  
                self.check()  
                self.turn = 'p1'    
            if self.end == 30:  
                Clock.schedule_once(self.game_over,1 ) 
  
    def check(self):  
        matched = []  
        for line in self.win:  
            if line[0].text and line[0].text == line[1].text == line[2].text:
                
                if line not in matched:
                    b1,b2,b3=line
                    self.highlight_line([b1,b2,b3])    
                    matched.append(line)  
  
        if matched:  
            self.win = [line for line in self.win if line not in matched]  
            points = len(matched)
            sound=SoundLoader.load('video-game-bonus-323603.mp3')
            sound.play()  
            if self.turn == 'p1':  
                self.p1s += points  
            else:  
                self.p2s += points  
  
            self.root.ids.play1.text = f'{self.pp1} [O] score\n{self.p1s}'  
            self.root.ids.play2.text = f'{self.pp2} [X] score\n{self.p2s}'
    def game_over(self,dt=None):
    	sound=SoundLoader.load('spin-complete-295086.mp3')
    	sound.play()
    	self.gameend = True
    	if self.p1s > self.p2s:
    		winner = self.pp1
    	elif self.p1s < self.p2s:
    		winner = self.pp2
    	else:
    		winner = None
    	content = MDBoxLayout(orientation="vertical", spacing="10dp", padding="10dp", adaptive_height=True, size_hint_y=None, height=180)
    	content.add_widget(MDIcon(
            icon="scale-balance" if winner is None else "trophy",
          font_size='64sp',
            size_hint=(None, None),
            size=("40dp", "40dp"),
            pos_hint={'center_x':0.5},
            theme_text_color="Custom",
            text_color=(1, 0.5, 0.2, 1),
        ))
    	content.add_widget(
    MDLabel(
         text=("Īt's @ T!ê" if winner is None else f"{winner} Wiñ$"),
       
        size_hint=(None, None),pos_hint={'center_x':0.5},
        size=('350dp', '120dp'),
        halign="center",
        markup=True,
        font_style='H4',
         font_size='40dp',
        theme_text_color="Primary",
    )
)

    	content.add_widget(MDRoundFlatIconButton(text="Play Again",icon='refresh', size_hint=(None,None), size=("50dp","15dp"),pos_hint={'center_x':0.5} ,on_release=lambda x: self.reset()))
    	content.add_widget(MDRoundFlatIconButton(text="Exit",icon="exit-to-app",pos_hint={'center_x':0.5} ,size_hint=(None,None), size=("50dp","15dp"), on_release=lambda x: self.stop()))
    	self.game_over_dialog = MDDialog(title="G∆m€ Ove®", type="custom",size_hint=(None,None),size=('300dp','400dp'), auto_dismiss=False, content_cls=content)
    	self.game_over_dialog.open()
if __name__ == '__main__':  
    mdApp().run()