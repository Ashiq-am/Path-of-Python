# Wait job item's share button appears
# in 5 seconds
job_share_btn_ele = _tab.wait_appear(
    locator.chrome.linkedin.jobitem.share_button, wait_timeout=2)

# If job item's share button exists, click
# the share button
if job_share_btn_ele:
    job_share_btn_ele.click()

    # Wait the copy link button appears in 5 seconds
    copy_link = _tab.wait_appear(
        locator.chrome.linkedin.jobitem.copy_link, wait_timeout=2)

    # If the copy link exists, click the copy
    # link to set clipboard data
    if copy_link:
        copy_link.click()

        # Sleep 0.2 second to wait the clipboard
        # in ready state
        sleep(0.2)

        # Get the job link string and save into
        # result object 'details'
        details["Job Link"] = get_clipboard_data()
