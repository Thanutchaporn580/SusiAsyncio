﻿# SusiAsyncio
# Choose asyncio to create a program about bank account work.
# สร้าง class BankAccount ใน class มี def __init__ เป็น constructor แล้วมีการกำหนดค่าเริ่มต้นของ balance ให้เท่ากับ 0 และสร้าง asyncio.Lock() เพื่อป้องกันการเข้าถึงข้อมูลพร้อมกัน มี method deposit ใช้ฝากเงิน มีการใช้ asyncio.Lock() เพื่อจัดการการเข้าถึงข้อมูลแบบไม่พร้อมกัน และใช้ asyncio.sleep(random.uniform(1, 3)) เพื่อจำลองเวลาการทำธุรกรรม มี method withdraw ใช้ถอนเงิน ใช้ if-else ตรวจสอบเงื่อนไขว่ามีเงินพอที่จะถอนมั้ย และใช้ asyncio.Lock() ด้วย 
# async def main() เป็น main function ใช้เพื่อเริ่มการทำงานของโปรแกรม มีการสร้าง object BankAccount ด้วยเงินเริ่มต้น 1000 มีการกำหนดธุรกรรมที่ทำ มีการจัดการการทำงานของธุรกรรมแบบไม่บล็อก โดยใช้ asyncio.gather() และแสดงผล Final balance ซึ่งคือยอดเงินสุดท้ายหลังจากทำธุรกรรมทั้งหมด
# asyncio.run(main()) : ฟังก์ชัน main() จะถูกเรียกใช้เมื่อไฟล์ถูกรันโดยตรงเท่านั้น
# To conclude, this program demonstrates how asyncio works to simulate the operation of a non-blocking bank account.
