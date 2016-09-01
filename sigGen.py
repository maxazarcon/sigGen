from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


class SigGen(Tk):
    def __init__(self):
        Tk.__init__(self)

        # Inputs
        self.fName = Entry(self, width=30)
        self.lName = Entry(self, width=30)
        self.dNumber = Entry(self, width=30)
        self.fNumber = Entry(self, width=30)
        self.pEmail = Entry(self, width=30)
        self.cEmail = Entry(self, width=30)
        self.photoURL = Entry(self, width=62)

        #Photo
        self.image = Image.open("img/rebdlogo.jpg")
        self.display = ImageTk.PhotoImage(image=self.image)
        self.imgLabel = Label(self, image=self.display)
        self.imgLabel.grid(row=0,columnspan=2)

        # Labels
        self.fNameLabel = Label(self, text="First Name\n")
        self.lNameLabel = Label(self, text="Last Name\n")
        self.dNumberLabel = Label(self, text="Direct Phone #\n")
        self.fNumberLabel = Label(self, text="Fax #\n")
        self.pEmailLabel = Label(self, text="Personal Email\n")
        self.cEmailLabel = Label(self, text="Company Email\n")
        self.photoURLLabel = Label(self, text="Agent Photo URL\n")
        self.signatureDone = Label(self, text="\nSignature created!", height=2)
        self.button = Button(self, text="Create Signature", command=self.on_button)
        self.exitButton = Button(self, text="Done", command=self.close_window)

        # Label Grid
        self.fNameLabel.grid(row=2, column=0)
        self.lNameLabel.grid(row=2, column=1)
        self.dNumberLabel.grid(row=4, column=0)
        self.fNumberLabel.grid(row=4, column=1)
        self.pEmailLabel.grid(row=6, column=0)
        self.cEmailLabel.grid(row=6, column=1)
        self.photoURLLabel.grid(row=8, columnspan=2)

        # Input Grid
        self.fName.grid(row=1, column=0)
        self.lName.grid(row=1, column=1)
        self.dNumber.grid(row=3, column=0)
        self.fNumber.grid(row=3, column=1)
        self.pEmail.grid(row=5, column=0)
        self.cEmail.grid(row=5, column=1)
        self.photoURL.grid(row=7, columnspan=2, column=0)
        self.button.grid(row=9, columnspan=2)

    def on_button(self):
        fd = filedialog.asksaveasfile(mode="w+", defaultextension=".html")
        if fd is None:
            return
        else:
            self.signatureDone.grid(row=10, columnspan=2)
            self.exitButton.grid(row=11, columnspan=2)

        fd.write(
            "<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.0 Transitional//EN\" \"http://www.w3.org/TR/REC-html40/loose.dtd\">\n" +
            "<html>\n" +
            "<head>\n" +
            "<meta https-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n" +
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n" +
            "<meta charset=\"UTF-8\">\n" +
            "<title>Real Estate by Design</title>\n" +
            "<style type=\"text/css\" media=\"all\">\n" +
            "p.ecxMsoNormal {\n" +
            "Margin: 0px;\n" +
            "Margin-bottom: 0px;\n" +
            "}\n" +
            "\n" +
            ".aBn {\n" +
            "border-bottom: none;\n" +
            "text-decoration: none;\n" +
            "}\n" +
            "    \n" +
            ".gc-cs-link {\n" +
            "text-decoration: none !important;\n" +
            "}\n" +
            "\n" +
            "div.gt a,\n" +
            "div.ii a[href] {}\n" +
            "\n" +
            ".widen {\n" +
            "width: 100%;\n" +
            "}\n" +
            "</style>\n" +
            "</head>\n" +
            "<body>\n" +
            "<table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" style=\"font-family: Tahoma, Geneva, sans-serif;" +
            "font-size: 1px; line-height: 2px; border-collapse: collapse; border-spacing: 0px; margin: 0px; padding: 0px;" +
            "\">\n" +
            "<tbody>\n" +
            "<tr>\n" +
            "<td style=\"font-size: 17px; line-height: 17px; height: 17px; margin: 0px; padding: 0px; display: block;\">\n" +
            "<div style=\"font-size: 17px; line-height: 17px; height: 17px; margin: 0px; padding: 0px; display: block;\">" +
            "</div>\n" +
            "</td>\n" +
            "</tr>\n" +
            "<tr>\n" +
            "<td style=\"font-size: 13px; line-height: 17px; color: #434343;\"><span style=\"text-decoration:none;\">" +
            "<font face=\"Tahoma, Geneva, sans-serif\" style=\"text-decoration:none !important;\">Kind regards,</font>" +
            "</span></td>\n" +
            "</tr>\n" +
            "<tr>\n" +
            "<td style=\"font-size: 17px; line-height: 17px; height: 17px; margin: 0px; padding: 0px; display: block;\">\n" +
            "<div style=\"font-size: 17px; line-height: 17px; height: 17px; margin: 0px; padding: 0px; display: block;\">" +
            "</div>\n" +
            "</td>\n" +
            "</tr>\n" +
            "<tr>\n" +
            "<td style=\"background-color: #1167ab; font-size: 10px; line-height: 10px; height: 10px; margin: 0px;" +
            " padding: 0px; display: block; background-position: initial initial; background-repeat: initial initial;\">\n" +
            "<div style=\"font-size: 10px; line-height: 10px; height: 10px; margin: 0px; padding: 0px; " +
            "display: block;\"></div>\n" +
            "</td>\n" +
            "</tr>\n" +
            "<tr>\n" +
            "<td style=\"background-color: #1167ab; background-position: initial initial; background-repeat: ""initial initial;\">\n" +
            "<table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" style=\"font-size: 13px; font-family: Tahoma, Geneva, sans-serif; text-align: left; border-spacing: 0px;\">\n" +
            "<tbody>\n" +
            "<tr>\n" +
            "<td style=\"line-height:1px;font-size:1px;width:10px;\" width=\"10\"></td>\n" +
            "<td style=\"font-size: 13px; color: #ffffff; line-height: 17px; font-weight: bold;\"> <span style=\"text-decoration:none;\"> <font face=\"Tahoma, Geneva, sans-serif\" color=\"#FFFFFF\" style=\"text-decoration:none !important;\">" + str(self.fName.get()) + " " + str(self.lName.get()) + "</font> </span> </td>\n" +
            "<td style=\"line-height:1px;font-size:1px;\" width=\"6\"></td>\n" +
            "<td valign=\"middle\" width=\"0\" style=\"font-size: 13px; text-align: center; font-weight: normal; color: #ffffff; line-height: 17px;\"> <span> <span> <font face=\"Tahoma, Geneva, sans-serif\">-</font> </span> </span>\n" +
            "</td>\n" +
            "<td style=\"line-height:1px;font-size:1px;\" width=\"6\"></td>\n" +
            "<td style=\"font-size: 13px; color: #ffffff; line-height: 17px;\"> <span style=\"text-decoration:none;\"><font face=\"Tahoma, Geneva, sans-serif\" color=\"#FFFFFF\" style=\"text-decoration:none !important;\"></font></span> </td>\n" +
            "<td style=\"line-height:1px;font-size:1px;width:10px;\" width=\"10\"></td>\n" +
            "</tr>\n" +
            "</tbody>\n" +
            "</table>\n" +
            "</td>\n" +
            "</tr>\n" +
            "<tr>\n" +
            "<td style=\"background-color: #1167ab; background-position: initial initial; background-repeat: initial initial;\">\n" +
            "<table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" style=\"font-size: 13px; font-family: Tahoma, Geneva, sans-serif; text-align: left; border-spacing: 0px;\">\n" +
            "<tbody>\n" +
            "<tr>\n" +
            "<td style=\"line-height:1px;font-size:1px;width:10px;\" width=\"10\"></td>\n" +
            "<td style=\"font-size: 11px; line-height: 17px; color: #ffffff; white-space: nowrap;\"> <span style=\"text-decoration:none;\"><font face=\"Tahoma, Geneva, sans-serif\" color=\"#FFFFFF\" style=\"text-decoration:none !important;\"></font></span> </td>\n" +
            "</tr>\n" +
            "</tbody>\n" +
            "</table>\n" +
            "</td>\n" +
            "</tr>\n" +
            "<tr>\n" +
            "<td valign=\"bottom\" style=\"background-color: #1167ab; background-position: initial initial; background-repeat: initial initial;\">\n" +
            "<table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" style=\"font-size: 13px; font-family: Tahoma, Geneva, sans-serif; text-align: left; border-spacing: 0px;\">\n" +
            "<tbody>\n" +
            "<tr>\n" +
            "<td style=\"line-height:1px;font-size:1px;width:10px;\" width=\"10\"></td>\n" +
            "<td height=\"17\" style=\"font-size: 13px; color: #ffffff; line-height: 17px; font-weight: bold;\">\n" +
            "<font face=\"Tahoma, Geneva, sans-serif\">Real Estate by Design</font>\n" +
            "</td>\n" +
            "<td style=\"font-size: 17px; line-height: 17px; height: 17px; margin: 0px; padding: 0px; display: block;\">\n" +
            "<div style=\"font-size: 17px; line-height: 17px; height: 17px; margin: 0px; padding: 0px; display: block;\"></div>\n" +
            "</td>\n" +
            "</tr>\n" +
            "</tbody>\n" +
            "</table>\n" +
            "</td>\n" +
            "</tr>\n" +
            "<tr>\n" +
            "<td style=\"background-color: #1167ab; font-size: 10px; line-height: 10px; height: 10px; margin: 0px; padding: 0px; display: block; background-position: initial initial; background-repeat: initial initial;\">\n" +
            "<div style=\"font-size: 10px; line-height: 10px; height: 10px; margin: 0px; padding: 0px; display: block;\"></div>\n" +
            "</td>\n" +
            "</tr>\n" +
            "<tr>\n" +
            "<td style=\"font-size: 17px; line-height: 17px; height: 17px; margin: 0px; padding: 0px; display: block;\">\n" +
            "<div style=\"font-size: 17px; line-height: 17px; height: 17px; margin: 0px; padding: 0px; display: block;\"></div>\n" +
            "</td>\n" +
            "</tr>\n" +
            "<tr>\n" +
            "<td>\n" +
            "<table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" style=\"font-size: 13px; font-family: Tahoma, Geneva, sans-serif; text-align: left; border-spacing: 0px;\">\n" +
            "<tbody>\n" +
            "<tr>\n" +
            "<td style=\"line-height:1px;font-size:1px;width:10px;\" width=\"10\"></td>\n" +
            "<td height=\"12\" style=\"font-size: 13px; color: #434343; line-height: 12px; font-style: italic;\">\n" +
            "<font face=\"Tahoma, Geneva, sans-serif\">A Boutique Real Estate Agency</font>\n" +
            "</td>\n" +
            "</tr>\n" +
            "</tbody>\n" +
            "</table>\n" +
            "</td>\n" +
            "</tr>\n" +
            "<tr>\n" +
            "<td style=\"font-size: 17px; line-height: 17px; height: 17px; margin: 0px; padding: 0px; display: block;\">\n" +
            "<div style=\"font-size: 17px; line-height: 17px; height: 17px; margin: 0px; padding: 0px; display: block;\"></div>\n" +
            "</td>\n" +
            "</tr>\n" +
            "<tr>\n" +
            "<td>\n" +
            "<table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" style=\"font-size: 13px; font-family: Tahoma, Geneva, sans-serif; text-align: left; border-spacing: 0px;\">\n" +
            "<tbody>\n" +
            "<tr>\n" +
            "<td style=\"line-height:1px;font-size:1px;\" width=\"10\"></td>\n" +
            "<td>\n" +
            "<table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" style=\"border-spacing:0px;\">\n" +
            "<tbody>\n" +
            "<tr>\n" +
            "<td valign=\"middle\"> <img width=\"106\" height=\"106\" src=\"" + str(self.photoURL.get()) + "\" style=\"border: none; display: block; width: 106px; height: 106px; border-radius: 100%;\"></td>\n" +
            "<td></td>\n" +
            "</tr>\n" +
            "</tbody>\n" +
            "</table>\n" +
            "</td>\n" +
            "<td style=\"line-height:1px;font-size:1px;\" width=\"15\"></td>\n" +
            "<td style=\"vertical-align:top;\">\n" +
            "..\n" +
            "<p></p>\n" +
            "<table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" style=\"font-size: 1px; line-height: 2px; font-family: Tahoma, Geneva, sans-serif; text-align: left; border-spacing: 0px;\">\n" +
            "<tbody>\n" +
            "<tr>\n" +
            "<td height=\"18\" style=\"font-size: 1px; color: #434343; line-height: 1px;\">\n" +
            "<table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" style=\"font-size: 13px; font-family: Tahoma, Geneva, sans-serif; text-align: left; border-spacing: 0px;\">\n" +
            "<tbody>\n" +
            "<tr>\n" +
            "<td width=\"89\" style=\"font-size: 13px; color: #1167ab; font-weight: bold; line-height: 17px;\">\n" +
            "<font face=\"Tahoma, Geneva, sans-serif\"> <span style=\"font-weight:normal;font-style:normal\">Direct</span> </font>\n" +
            "</td>\n" +
            "<td style=\"font-size: 13px; color: #434343; line-height: 17px; font-weight: bold;\">\n" +
            "<font face=\"Tahoma, Geneva, sans-serif\">" + str(self.dNumber.get()) + "</font>\n" +
            "</td>\n" +
            "</tr>\n" +
            "</tbody>\n" +
            "</table>\n" +
            "</td>\n" +
            "</tr>\n" +
            "<tr>\n" +
            "<td height=\"18\" style=\"font-size: 1px; color: #434343; line-height: 1px;\">\n" +
            "<table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" style=\"font-size: 13px; font-family: Tahoma, Geneva, sans-serif; text-align: left; border-spacing: 0px;\">\n" +
            "<tbody>\n" +
            "<tr>\n" +
            "<td width=\"89\" style=\"font-size: 13px; color: #1167ab; font-weight: bold; line-height: 17px;\">\n" +
            "<font face=\"Tahoma, Geneva, sans-serif\"> <span style=\"font-weight:normal;font-style:normal\">Fax</span> </font>\n" +
            "</td>\n" +
            "<td style=\"font-size: 13px; color: #434343; line-height: 17px;\">\n" +
            "<font face=\"Tahoma, Geneva, sans-serif\">" + str(self.fNumber.get()) + "</font>\n" +
            "</td>\n" +
            "</tr>\n" +
            "</tbody>\n" +
            "</table>\n" +
            "</td>\n" +
            "</tr>\n" +
            "<tr>\n" +
            "<td height=\"18\" style=\"font-size: 1px; color: #434343; line-height: 1px;\">\n" +
            "<table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" style=\"font-size: 13px; font-family: Tahoma, Geneva, sans-serif; text-align: left; border-spacing: 0px;\">\n" +
            "<tbody>\n" +
            "<tr>\n" +
            "<td width=\"89\" style=\"font-size: 13px; color: #1167ab; font-weight: bold; line-height: 17px;\">\n" +
            "<font face=\"Tahoma, Geneva, sans-serif\"> <span style=\"font-weight:normal;font-style:normal\">Email</span> </font>\n" +
            "</td>\n" +
            "<td style=\"font-size: 13px; color: #434343; line-height: 17px; font-weight: bold;\">\n" +
            "<font face=\"Tahoma, Geneva, sans-serif\"><a href=\"mailto:" + str(self.pEmail.get()) + "\" target=\"_blank\" style=\"color: #434343; text-decoration: none;\">" + str(self.pEmail.get()) + "</a></font>\n" +
            "</td>\n" +
            "</tr>\n" +
            "</tbody>\n" +
            "</table>\n" +
            "</td>\n" +
            "</tr>\n" +
            "<tr>\n" +
            "<td height=\"18\" style=\"font-size: 1px; color: #434343; line-height: 1px;\">\n" +
            "<table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" style=\"font-size: 13px; font-family: Tahoma, Geneva, sans-serif; text-align: left; border-spacing: 0px;\">\n" +
            "<tbody>\n" +
            "<tr>\n" +
            "<td width=\"89\" style=\"font-size: 13px; color: #1167ab; font-weight: bold; line-height: 17px;\">\n" +
            "<font face=\"Tahoma, Geneva, sans-serif\"> <span style=\"font-weight:normal;font-style:normal\">Company</span> </font>\n" +
            "</td>\n" +
            "<td style=\"font-size: 13px; color: #434343; line-height: 17px; font-weight: bold;\">\n" +
            "<font face=\"Tahoma, Geneva, sans-serif\"><a href=\"mailto:" + str(self.cEmail.get()) + "\" target=\"_blank\" style=\"color: #434343; text-decoration: none;\">" + str(self.cEmail.get()) + "</a></font>\n" +
            "</td>\n" +
            "</tr>\n" +
            "</tbody>\n" +
            "</table>\n" +
            "</td>\n" +
            "</tr>\n" +
            "</tbody>\n" +
            "</table>\n" +
            "</td>\n" +
            "</tr>\n" +
            "</tbody>\n" +
            "</table>\n" +
            "</td>\n" +
            "</tr>\n" +
            "</tbody>\n" +
            "</table>\n" +
            "</body>\n" +
            "</html>"
            )

    def close_window(self):
        sys.exit()

app = SigGen()
app.wm_title("REBD Email Signature Generator")
app.resizable(width=False, height=False)
app.geometry('{}x{}'.format(445,450))
app.call("wm", "attributes", ".", "-topmost", "1")
app.lift()
app.mainloop()
