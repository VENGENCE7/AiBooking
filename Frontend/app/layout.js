import "./globals.css";
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Booked AI",
  description: "Booked Ai POC",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body
        className={inter.className}
        style={{
          margin: "30px",
        }}
      >
        {children}
      </body>
    </html>
  );
}
